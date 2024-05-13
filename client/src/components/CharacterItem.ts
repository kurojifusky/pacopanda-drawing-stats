import { LitElement, html } from "lit"
import { customElement, property } from "lit/decorators.js"
import { ifDefined } from "lit/directives/if-defined.js"

@customElement("pds-character-item")
export class CharacterItem extends LitElement {
  @property({ type: String })
  avatar?: string

  @property({ type: String })
  name?: string

  @property({ type: String })
  subtext?: string

  @property({ type: String })
  subtextLink?: string

  render() {
    return html`<div class="flex items-center">
      <img src="${ifDefined(this.avatar)}" class="flex-shrink-0 size-32" />
      <div class="flex">
        <span>${this.name}</span>
        ${!this.subtextLink
          ? html`<a href=${ifDefined(this.subtextLink)}>${this.subtext}</a>`
          : html`<span>${this.subtext}</span>`}
      </div>
    </div>`
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "pds-character-item": CharacterItem
  }
}
