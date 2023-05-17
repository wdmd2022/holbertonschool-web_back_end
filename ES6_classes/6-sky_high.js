import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }
  // needs a getter for each attribute but the sqft getter is in the super //
  get floors() {
    return (this._floors);
  }
  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this._floors} floors`);
  }
}
