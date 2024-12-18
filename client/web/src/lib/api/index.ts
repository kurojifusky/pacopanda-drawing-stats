import type { EndpointRequiresAuth } from "./params.types"
import type {
  ArtworkMultiResponse,
  ArtworkResponse,
  CharacterMultiResponse,
  CharacterResponse,
  ServerStatusResponse,
} from "./responses.types"
import { env } from "$env/dynamic/private"

const endpoint = {
  stats: "/stats",
  status: "/status",
  artwork: "/artwork",
  artworks: "/artworks",
  character: "/character",
  characters: "/characters",
  newArtwork: "/new/artwork",
  newCharacter: "/new/character",
} as const

const fetchWrapper = async <T extends object>(
  endpoint: string,
  options?: RequestInit,
) => {
  return (await fetch(
    `${env.SERVER_HOSTNAME || "http://localhost:4000"}${endpoint}`,
    options,
  ),
  options) as unknown as Promise<T>
}

export const serverStatus = async () => {
  return await fetchWrapper<ServerStatusResponse>(endpoint.status)
}

export const artwork = {
  getOne: async () => {
    return await fetchWrapper<ArtworkResponse>(endpoint.artwork)
  },
  getMulti: async <P extends number[] = [number]>() => {
    return await fetchWrapper<ArtworkMultiResponse<P>>(endpoint.artworks)
  },
  /**
   * Requires an auth token and accepts POST requests only
   */
  post: async ({ token_key }: EndpointRequiresAuth) => {
    return await fetchWrapper(endpoint.newCharacter, { method: "POST" })
  },
}

export const character = {
  getOne: async () => {
    return await fetchWrapper<CharacterResponse>(endpoint.character)
  },
  getMulti: async <P extends number[] = [number]>() => {
    return await fetchWrapper<CharacterMultiResponse<P>>(endpoint.characters)
  },
  /**
   * Requires an auth token and accepts POST requests only
   */
  post: async ({ token_key }: EndpointRequiresAuth) => {
    return await fetchWrapper(endpoint.newArtwork, { method: "POST" })
  },
}
