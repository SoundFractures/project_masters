from Orange.data import Table, Domain
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class MyWidget(OWWidget):
    name = "Hello Interactive"
    description = "HITL Interactive Decision Tree Builder"
    icon = "icons/interactive.svg"
    priority = 100
    keywords = ["widget", "data"]
    want_main_area = False
    resizing_enabled = False

    label = Setting("")

    class Inputs:
        data = Input("Data", Table)

    class Outputs:
        data = Output("Data", Table, default=True)

    class Warning(OWWidget.Warning):
        warning = Msg("My warning!")

    def __init__(self):
        super().__init__()
        self.data = None
        self.tree_model = None
        self.feature_names = None

        self.label_box = gui.lineEdit(
            self.controlArea, self, "label", box="Text", callback=self.commit
        )

        self.build_tree_button = gui.button(
            self.controlArea,
            self,
            "Build Decision Tree",
            callback=self.build_decision_tree,
        )

    @Inputs.data
    def set_data(self, data):
        if data:
            self.data = data
            self.feature_names = [var.name for var in data.domain.attributes]
        else:
            self.data = None

    def build_decision_tree(self):
        if self.data is None:
            self.Warning.warning("No data provided.")
            return

        # print the head of the data
        print(self.data[:5])

        # Example: Split the data into training and testing sets
        train_data, test_data = train_test_split(
            self.data, test_size=0.2, random_state=42
        )

        # Example: Build a decision tree classifier
        self.tree_model = DecisionTreeClassifier()
        self.tree_model.fit(train_data.X, train_data.Y)

        # Example: Make predictions on the test set
        predictions = self.tree_model.predict(test_data.X)

        # Example: Evaluate the accuracy
        accuracy = accuracy_score(test_data.Y, predictions)

        # Provide feedback or update the UI based on the results
        self.report_caption(f"Decision Tree Accuracy: {accuracy:.2f}")

        # Optionally, you can send the trained model as output
        self.Outputs.data.send(self.tree_model)

    def commit(self):
        # Additional logic to handle user input or updates
        pass

    def send_report(self):
        # Additional reporting logic
        pass
