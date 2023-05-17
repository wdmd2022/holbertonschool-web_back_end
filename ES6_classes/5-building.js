export default class Building {
  // this is an abstract class that will be extended //
  constructor(sqft) {
    if (typeof sqft === 'number') {
      this._sqft = sqft;
    }
    if ((this.constructor.name !== 'Building') && (!this.evacuationWarningMessage)) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // getter time! //
  get sqft() {
    return (this._sqft);
  }
}
