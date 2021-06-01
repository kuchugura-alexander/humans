function GlobalState(initialValue) {
    this.value = initialValue;  // Actual value of a global state
    this.subscribers = [];     // List of subscribers
    this.host = `http://localhost:8000`
    // this.host = `https://human.cloudsockets.net`

    this.getValue = function () {
        return this.value;
    }

    this.getHost = function () {
        return this.host;
    }

    this.setHost = function (newHost) {
        if (this.getHost() === newHost) {
            return
        }

        this.host = newHost;
        this.subscribers.forEach(subscriber => {
            subscriber(this.host);
        });
    }

    this.setValue = function (newState) {
        if (this.getValue() === newState) {
            return
        }

        this.value = newState;
        this.subscribers.forEach(subscriber => {
            subscriber(this.value);
        });
    }

    this.subscribe = function (itemToSubscribe) {
        if (this.subscribers.indexOf(itemToSubscribe) > -1) {
            return
        }
        // Subscribe a component
        this.subscribers.push(itemToSubscribe);
    }

    this.unsubscribe = function (itemToUnsubscribe) {
        this.subscribers = this.subscribers.filter(
            subscriber => subscriber !== itemToUnsubscribe
        );
    }
}
export default GlobalState;
