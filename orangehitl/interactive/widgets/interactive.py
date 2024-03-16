import numpy as np
import Orange.data
from orangewidget.widget import OWBaseWidget, Input, Output
from orangewidget.utils.widgetpreview import WidgetPreview
from orangewidget import gui

from orangehitl.interactive.cart.cart import (
    train_cart_model,
)  # Importing the function from cart.py


class OWInteractive(OWBaseWidget):
    name = "Interactive"
    description = "Interactive description"
    icon = "icons/interactive.svg"
    priority = 10

    class Inputs:
        data = Input("Data", Orange.data.Table)

    class Outputs:
        sample = Output("Sampled Data", Orange.data.Table)

    want_main_area = False

    def __init__(self):
        super().__init__()

        # GUI
        box = gui.widgetBox(self.controlArea, "Info")
        self.infoa = gui.widgetLabel(
            box, "No data on input yet, waiting to get something."
        )
        self.infob = gui.widgetLabel(box, "")

        # Button 
        self.recreate_button = gui.button(
            self.controlArea,
            self,
            "Recreate",
            callback=self.recreate_model
        )

    @Inputs.data
    def set_data(self, dataset):
        if dataset is not None:
            # Preprocess data if needed
            X = dataset.X
            y = dataset.Y

            # Train CART model
            cart_model = train_cart_model(X, y)

            # Do something with the trained model
            # For example, print the feature importances
            print("Feature Importances:", cart_model.feature_importances_)

        else:
            self.infoa.setText("No data on input yet, waiting to get something.")
            self.infob.setText("")
            self.Outputs.sample.send("Sampled Data")

    def recreate_model(self):
        # Do something when the button is clicked
        print("Recreating 321")


if __name__ == "__main__":
    WidgetPreview(OWInteractive).run(Orange.data.Table("iris"))
