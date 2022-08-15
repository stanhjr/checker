from typing import Optional
from pydantic import BaseModel


class SocialMedia(BaseModel):
    registered: Optional[bool]


class DomainDetails(BaseModel):
    registered: Optional[bool]


class BreachDetails(BaseModel):
    first_breach: Optional[str]


class History(BaseModel):
    first_seen: int


class AccountDetails(BaseModel):
    adobe: SocialMedia
    airbnb: SocialMedia
    amazon: SocialMedia
    apple: SocialMedia
    archiveorg: SocialMedia
    atlassian: SocialMedia
    booking: SocialMedia
    bukalapak: SocialMedia
    discord: SocialMedia
    disneyplus: SocialMedia
    ebay: SocialMedia
    envato: SocialMedia
    evernote: SocialMedia
    facebook: SocialMedia
    flickr: SocialMedia
    flipkart: SocialMedia
    foursquare: SocialMedia
    github: SocialMedia
    google: SocialMedia
    gravatar: SocialMedia
    imgur: SocialMedia
    instagram: SocialMedia
    jdid: SocialMedia
    kakao: SocialMedia
    lastfm: SocialMedia
    lazada: SocialMedia
    linkedin: SocialMedia
    mailru: SocialMedia
    microsoft: SocialMedia
    myspace: SocialMedia
    netflix: SocialMedia
    ok: SocialMedia
    patreon: SocialMedia
    pinterest: SocialMedia
    quora: SocialMedia
    qzone: SocialMedia
    rambler: SocialMedia
    samsung: SocialMedia
    skype: SocialMedia
    spotify: SocialMedia
    tokopedia: SocialMedia
    tumblr: SocialMedia
    twitter: SocialMedia
    vimeo: SocialMedia
    weibo: SocialMedia
    wordpress: SocialMedia
    yahoo: SocialMedia
    zoho: SocialMedia


class EmailCheckerScraper(BaseModel):
    deliverable: Optional[bool]
    email: str
    score: float
    account_details: AccountDetails
    breach_details: BreachDetails
    history: History
    domain_details: DomainDetails


class EmailCheckerIpQuality(BaseModel):
    valid: Optional[bool]
    domain_velocity: Optional[str]

