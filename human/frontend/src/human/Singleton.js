function GlobalState(initialValue) {
    this.value = initialValue;  // Actual value of a global state
    this.subscribers = [];     // List of subscribers
    this.host = `http://localhost:8000`
    // this.host = `https://human.cloudsockets.net`

    this.getValue = function () {
        // Get the actual value of a global state
        return this.value;
    }

    this.getHost = function () {
        // Get the actual value of a global state
        return this.host;
    }

    this.setValue = function (newState) {
        // This is a method for updating a global state

        if (this.getValue() === newState) {
            // No new update
            return
        }

        this.value = newState;  // Update global state value
        this.subscribers.forEach(subscriber => {
            // Notify subscribers that the global state has changed
            subscriber(this.value);
        });
    }

    this.subscribe = function (itemToSubscribe) {
        // This is a function for subscribing to a global state
        if (this.subscribers.indexOf(itemToSubscribe) > -1) {
            // Already subsribed
            return
        }
        // Subscribe a component
        this.subscribers.push(itemToSubscribe);
    }

    this.unsubscribe = function (itemToUnsubscribe) {
        // This is a function for unsubscribing from a global state
        this.subscribers = this.subscribers.filter(
            subscriber => subscriber !== itemToUnsubscribe
        );
    }
}
export default GlobalState;

// const count = new GlobalState(0);