from Dashboard import Dashboard
from Weather import Weather

if __name__ == "__main__":
    mainDashboard = Dashboard("main")
    mobileDashboard = Dashboard("Mobile")

    weatherDublin = Weather("Dublin")
    weatherMadrid = Weather("Madrid")
    weatherNY = Weather("New York")

    weatherNY.attach_observer(mobileDashboard)
    weatherDublin.attach_observer(mobileDashboard)

    weatherNY.attach_observer(mainDashboard)
    weatherDublin.attach_observer(mainDashboard)
    weatherMadrid.attach_observer(mainDashboard)

    #changes happens and observers are notified
    weatherMadrid.notify_changes("27°C")
    weatherDublin.notify_changes("15°C")
    weatherNY.notify_changes("9°C")
