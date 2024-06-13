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

export const getServerStatus = async () => {
  return await fetchWrapper<ServerStatusResponse>(endpoint.status)
}

export const getArtwork = async () => {
  return await fetchWrapper<ArtworkResponse>(endpoint.artwork)
}

export const getArtworks = async <P extends number[] = [number]>() => {
  return await fetchWrapper<ArtworkMultiResponse<P>>(endpoint.artworks)
}

export const getCharacter = async () => {
  return await fetchWrapper<CharacterResponse>(endpoint.character)
}

export const getCharacters = async <P extends number[] = [number]>() => {
  return await fetchWrapper<CharacterMultiResponse<P>>(endpoint.characters)
}

/**
 * Requires an auth token and accepts POST requests only
 */
export const postNewCharacters = async ({
  token_key,
}: EndpointRequiresAuth) => {
  return await fetchWrapper(endpoint.newArtwork, { method: "POST" })
}
/**
 * Requires an auth token and accepts POST requests only
 */
export const postNewArtworks = async ({ token_key }: EndpointRequiresAuth) => {
  return await fetchWrapper(endpoint.newArtwork, { method: "POST" })
}
