/* eslint-disable @typescript-eslint/member-delimiter-style */
export const endpoints = {
  artwork: "/artwork",
  artworks: "/artworks",
  character: "/character",
  characters: "/characters",
  /**
   * Requires an auth token and accepts POST requests only
   */
  newArtwork: "/new/artwork",
  /**
   * Requires an auth token and accepts POST requests only
   */
  newCharacter: "/new/character",
} as const

export namespace PandaPacoDrawings {
  /**
   * Identifies a plot of data to be visualized via a bar or line graph
   *
   * @param DataPlot Accepts only number type from a constrained array of numbers
   */
  export interface TimeSeriesData<DataPlot extends number[] = [number]> {
    date: string | Date
    data_count: DataPlot
    data_average?: DataPlot | null
  }
  /**
   * Returns the stats of all the artworks and characters accumulated,
   * and a time series data for previous years to be parsed by a compatible chart library
   *
   * @param Data Defaults to type `ArtworkResponse`
   */
  export interface StatisticsResponse<Data = ArtworkResponse> {
    total_artworks: number
    total_characters: number
    data?: {
      [year: number]: Array<TimeSeriesData & Data>
    }
  }
  /**
   * Returns the server's current status and uptime
   */
  export interface ServerStatusResponse {
    response: string
    uptime: string
  }
  /**
   * Returns a character and its recent appearances from artworks
   */
  export interface CharacterResponse {
    name: string
    avatar_url: string
    full_name?: string
    species: string
    is_hybrid: boolean
    recent_appearances: Omit<ArtworkResponse, "characters">[]
    first_appearance: Omit<ArtworkResponse, "characters">
    plot?: TimeSeriesData[]
  }
  /**
   * Returns a list of characters and its recent appearances from artworks
   *
   * @param ExtendPlot Extends from `TimeSeriesData<DataPlot>`
   */
  export interface CharacterMultiResponse<ExtendPlot extends number[]> {
    characters: Omit<CharacterResponse, "plot">[]
    plot?: TimeSeriesData<ExtendPlot>[]
  }
  /**
   * Returns an artwork and its characters linked to it
   */
  export interface ArtworkResponse {
    title: string
    description: string
    mediums: string[] | never[]
    characters: Omit<
      CharacterResponse,
      "recent_appearances" | "first_appearance"
    >[]
    plot?: TimeSeriesData[]
  }
  /**
   * Returns a list of artworks and its characters linked to it
   *
   * @param ExtendPlot Extends from `TimeSeriesData<DataPlot>`
   */
  export interface ArtworkMultiResponse<ExtendPlot extends number[]> {
    artworks: Omit<ArtworkResponse, "plot">[]
    plot?: TimeSeriesData<ExtendPlot>[]
  }
}
