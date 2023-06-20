# Design Pattern Assignment

## Weather Monitoring

- Created weather station class which contains the utilities to add and remove observers, update weather stats and update the observers with new data.
- The observers have an abstract method called update.
- Since currently we are working only on display devices a separate entity of display devices which inherits observers is created.
- Then each display device implements its own version of update.
- The main class creates one device for each class and adds all of them to a weather station. The weather is updated and all notifications are shown.

----

## Vehicle Manufacturing

- Created vehicle class to incorporate base details of vehicles. It contains abstract method `display_details` to show the specs of vehicle.
- Car, Truck & Motorcycle classes inherit vehicle class and have their own display details function.
- There is separate factory class which has abstract `create_vehicle` method. Each vehicle has its own factory which implementation of the method.
- The main class imports all the factories and creates vehicles whenever it is called.