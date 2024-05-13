import { LitElement, css, html } from "lit"
import { customElement, property } from "lit/decorators.js"

@customElement("d3-line-graph-wrapper")
export class D3LineGraph extends LitElement {
  // TODO use d3.js to render stuff instead of chart.js
  static styles = css``

  @property({ type: Object })
  graphData?: object

  render() {
    return html`<canvas></canvas>`
  }

  connectedCallback() {
    super.connectedCallback()
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "d3-line-graph-wrapper": D3LineGraph
  }
}
