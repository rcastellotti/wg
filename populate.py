from app import db, Listing
import nanoid
from lorem import get_word, get_sentence
import random
import itertools
import datetime
from faker import Faker

fake=Faker(["en_US"])


wes = [
    "Royal2q0",
    "Royal2q1",
    "Royal2q2",
    "Royal2q3",
    "Royal2q4",
    "Zissou1q1",
    "GrandBudapest2q3", 
    "BottleRocket2q1",
    "GrandBudapest1q3",
    "IsleofDogs1q0",
]
icons = [
    "123",
    "activity",
    "alarm-fill",
    "alarm",
    "align-bottom",
    "align-center",
    "align-end",
    "align-middle",
    "align-start",
    "align-top",
    "alt",
    "app-indicator",
    "apple",
    "app",
    "archive-fill",
    "archive",
    "arrow-90deg-down",
    "arrow-90deg-left",
    "arrow-90deg-right",
    "arrow-90deg-up",
    "arrow-bar-down",
    "arrow-bar-left",
    "arrow-bar-right",
    "arrow-bar-up",
    "arrow-clockwise",
    "arrow-counterclockwise",
    "arrow-down-circle-fill",
    "arrow-down-circle",
    "arrow-down-left-circle-fill",
    "arrow-down-left-circle",
    "arrow-down-left-square-fill",
    "arrow-down-left-square",
    "arrow-down-left",
    "arrow-down-right-circle-fill",
    "arrow-down-right-circle",
    "arrow-down-right-square-fill",
    "arrow-down-right-square",
    "arrow-down-right",
    "arrow-down-short",
    "arrow-down-square-fill",
    "arrow-down-square",
    "arrow-down",
    "arrow-down-up",
    "arrow-left-circle-fill",
    "arrow-left-circle",
    "arrow-left-right",
    "arrow-left-short",
    "arrow-left-square-fill",
    "arrow-left-square",
    "arrow-left",
    "arrow-repeat",
    "arrow-return-left",
    "arrow-return-right",
    "arrow-right-circle-fill",
    "arrow-right-circle",
    "arrow-right-short",
    "arrow-right-square-fill",
    "arrow-right-square",
    "arrow-right",
    "arrows-angle-contract",
    "arrows-angle-expand",
    "arrows-collapse",
    "arrows-expand",
    "arrows-fullscreen",
    "arrows-move",
    "arrow-up-circle-fill",
    "arrow-up-circle",
    "arrow-up-left-circle-fill",
    "arrow-up-left-circle",
    "arrow-up-left-square-fill",
    "arrow-up-left-square",
    "arrow-up-left",
    "arrow-up-right-circle-fill",
    "arrow-up-right-circle",
    "arrow-up-right-square-fill",
    "arrow-up-right-square",
    "arrow-up-right",
    "arrow-up-short",
    "arrow-up-square-fill",
    "arrow-up-square",
    "arrow-up",
    "aspect-ratio-fill",
    "aspect-ratio",
    "asterisk",
    "at",
    "award-fill",
    "award",
    "backspace-fill",
    "backspace-reverse-fill",
    "backspace-reverse",
    "backspace",
    "back",
    "badge-3d-fill",
    "badge-3d",
    "badge-4k-fill",
    "badge-4k",
    "badge-8k-fill",
    "badge-8k",
    "badge-ad-fill",
    "badge-ad",
    "badge-ar-fill",
    "badge-ar",
    "badge-cc-fill",
    "badge-cc",
    "badge-hd-fill",
    "badge-hd",
    "badge-tm-fill",
    "badge-tm",
    "badge-vo-fill",
    "badge-vo",
    "badge-vr-fill",
    "badge-vr",
    "badge-wc-fill",
    "badge-wc",
    "bag-check-fill",
    "bag-check",
    "bag-dash-fill",
    "bag-dash",
    "bag-fill",
    "bag-plus-fill",
    "bag-plus",
    "bag",
    "bag-x-fill",
    "bag-x",
    "bandaid-fill",
    "bandaid",
    "bank2",
    "bank",
    "bar-chart-fill",
    "bar-chart-line-fill",
    "bar-chart-line",
    "bar-chart-steps",
    "bar-chart",
    "basket2-fill",
    "basket2",
    "basket3-fill",
    "basket3",
    "basket-fill",
    "basket",
    "battery-charging",
    "battery-full",
    "battery-half",
    "battery",
    "behance",
    "bell-fill",
    "bell-slash-fill",
    "bell-slash",
    "bell",
    "bezier2",
    "bezier",
    "bicycle",
    "binoculars-fill",
    "binoculars",
    "blockquote-left",
    "blockquote-right",
    "bluetooth",
    "body-text",
    "book-fill",
    "book-half",
    "bookmark-check-fill",
    "bookmark-check",
    "bookmark-dash-fill",
    "bookmark-dash",
    "bookmark-fill",
    "bookmark-heart-fill",
    "bookmark-heart",
    "bookmark-plus-fill",
    "bookmark-plus",
    "bookmarks-fill",
    "bookmarks",
    "bookmark-star-fill",
    "bookmark-star",
    "bookmark",
    "bookmark-x-fill",
    "bookmark-x",
    "bookshelf",
    "book",
    "boombox-fill",
    "boombox",
    "bootstrap-fill",
    "bootstrap-icons",
    "bootstrap-reboot",
    "bootstrap",
    "border-all",
    "border-bottom",
    "border-center",
    "border-inner",
    "border-left",
    "border-middle",
    "border-outer",
    "border-right",
    "border-style",
    "border",
    "border-top",
    "border-width",
    "bounding-box-circles",
    "bounding-box",
    "box-arrow-down-left",
    "box-arrow-down-right",
    "box-arrow-down",
    "box-arrow-in-down-left",
    "box-arrow-in-down-right",
    "box-arrow-in-down",
    "box-arrow-in-left",
    "box-arrow-in-right",
    "box-arrow-in-up-left",
    "box-arrow-in-up-right",
    "box-arrow-in-up",
    "box-arrow-left",
    "box-arrow-right",
    "box-arrow-up-left",
    "box-arrow-up-right",
    "box-arrow-up",
    "boxes",
    "box-seam",
    "box",
    "braces",
    "bricks",
    "briefcase-fill",
    "briefcase",
    "brightness-alt-high-fill",
    "brightness-alt-high",
    "brightness-alt-low-fill",
    "brightness-alt-low",
    "brightness-high-fill",
    "brightness-high",
    "brightness-low-fill",
    "brightness-low",
    "broadcast-pin",
    "broadcast",
    "brush-fill",
    "brush",
    "bucket-fill",
    "bucket",
    "bug-fill",
    "bug",
    "building",
    "bullseye",
    "calculator-fill",
    "calculator",
    "calendar2-check-fill",
    "calendar2-check",
    "calendar2-date-fill",
    "calendar2-date",
    "calendar2-day-fill",
    "calendar2-day",
    "calendar2-event-fill",
    "calendar2-event",
    "calendar2-fill",
    "calendar2-minus-fill",
    "calendar2-minus",
    "calendar2-month-fill",
    "calendar2-month",
    "calendar2-plus-fill",
    "calendar2-plus",
    "calendar2-range-fill",
    "calendar2-range",
    "calendar2",
    "calendar2-week-fill",
    "calendar2-week",
    "calendar2-x-fill",
    "calendar2-x",
    "calendar3-event-fill",
    "calendar3-event",
    "calendar3-fill",
    "calendar3-range-fill",
    "calendar3-range",
    "calendar3",
    "calendar3-week-fill",
    "calendar3-week",
    "calendar4-event",
    "calendar4-range",
    "calendar4",
    "calendar4-week",
    "calendar-check-fill",
    "calendar-check",
    "calendar-date-fill",
    "calendar-date",
    "calendar-day-fill",
    "calendar-day",
    "calendar-event-fill",
    "calendar-event",
    "calendar-fill",
    "calendar-minus-fill",
    "calendar-minus",
    "calendar-month-fill",
    "calendar-month",
    "calendar-plus-fill",
    "calendar-plus",
    "calendar-range-fill",
    "calendar-range",
    "calendar",
    "calendar-week-fill",
    "calendar-week",
    "calendar-x-fill",
    "calendar-x",
    "camera2",
    "camera-fill",
    "camera-reels-fill",
    "camera-reels",
    "camera",
    "camera-video-fill",
    "camera-video-off-fill",
    "camera-video-off",
    "camera-video",
    "capslock-fill",
    "capslock",
    "card-checklist",
    "card-heading",
    "card-image",
    "card-list",
    "card-text",
    "caret-down-fill",
    "caret-down-square-fill",
    "caret-down-square",
    "caret-down",
    "caret-left-fill",
    "caret-left-square-fill",
    "caret-left-square",
    "caret-left",
    "caret-right-fill",
    "caret-right-square-fill",
    "caret-right-square",
    "caret-right",
    "caret-up-fill",
    "caret-up-square-fill",
    "caret-up-square",
    "caret-up",
    "cart2",
    "cart3",
    "cart4",
    "cart-check-fill",
    "cart-check",
    "cart-dash-fill",
    "cart-dash",
    "cart-fill",
    "cart-plus-fill",
    "cart-plus",
    "cart",
    "cart-x-fill",
    "cart-x",
    "cash-coin",
    "cash-stack",
    "cash",
    "cast",
    "chat-dots-fill",
    "chat-dots",
    "chat-fill",
    "chat-left-dots-fill",
    "chat-left-dots",
    "chat-left-fill",
    "chat-left-quote-fill",
    "chat-left-quote",
    "chat-left",
    "chat-left-text-fill",
    "chat-left-text",
    "chat-quote-fill",
    "chat-quote",
    "chat-right-dots-fill",
    "chat-right-dots",
    "chat-right-fill",
    "chat-right-quote-fill",
    "chat-right-quote",
    "chat-right",
    "chat-right-text-fill",
    "chat-right-text",
    "chat-square-dots-fill",
    "chat-square-dots",
    "chat-square-fill",
    "chat-square-quote-fill",
    "chat-square-quote",
    "chat-square",
    "chat-square-text-fill",
    "chat-square-text",
    "chat",
    "chat-text-fill",
    "chat-text",
    "check2-all",
    "check2-circle",
    "check2-square",
    "check2",
    "check-all",
    "check-circle-fill",
    "check-circle",
    "check-lg",
    "check-square-fill",
    "check-square",
    "check",
    "chevron-bar-contract",
    "chevron-bar-down",
    "chevron-bar-expand",
    "chevron-bar-left",
    "chevron-bar-right",
    "chevron-bar-up",
    "chevron-compact-down",
    "chevron-compact-left",
    "chevron-compact-right",
    "chevron-compact-up",
    "chevron-contract",
    "chevron-double-down",
    "chevron-double-left",
    "chevron-double-right",
    "chevron-double-up",
    "chevron-down",
    "chevron-expand",
    "chevron-left",
    "chevron-right",
    "chevron-up",
    "circle-fill",
    "circle-half",
    "circle-square",
    "circle",
    "clipboard-check",
    "clipboard-data",
    "clipboard-minus",
    "clipboard-plus",
    "clipboard",
    "clipboard-x",
    "clock-fill",
    "clock-history",
    "clock",
    "cloud-arrow-down-fill",
    "cloud-arrow-down",
    "cloud-arrow-up-fill",
    "cloud-arrow-up",
    "cloud-check-fill",
    "cloud-check",
    "cloud-download-fill",
    "cloud-download",
    "cloud-drizzle-fill",
    "cloud-drizzle",
    "cloud-fill",
    "cloud-fog2-fill",
    "cloud-fog2",
    "cloud-fog-fill",
    "cloud-fog",
    "cloud-hail-fill",
    "cloud-hail",
    "cloud-haze2-fill",
    "cloud-haze2",
    "cloud-haze-fill",
    "cloud-haze",
    "cloud-lightning-fill",
    "cloud-lightning-rain-fill",
    "cloud-lightning-rain",
    "cloud-lightning",
    "cloud-minus-fill",
    "cloud-minus",
    "cloud-moon-fill",
    "cloud-moon",
    "cloud-plus-fill",
    "cloud-plus",
    "cloud-rain-fill",
    "cloud-rain-heavy-fill",
    "cloud-rain-heavy",
    "cloud-rain",
    "clouds-fill",
    "cloud-slash-fill",
    "cloud-slash",
    "cloud-sleet-fill",
    "cloud-sleet",
    "cloud-snow-fill",
    "cloud-snow",
    "clouds",
    "cloud-sun-fill",
    "cloud-sun",
    "cloud",
    "cloud-upload-fill",
    "cloud-upload",
    "cloudy-fill",
    "cloudy",
    "code-slash",
    "code-square",
    "code",
    "coin",
    "collection-fill",
    "collection-play-fill",
    "collection-play",
    "collection",
    "columns-gap",
    "columns",
    "command",
    "compass-fill",
    "compass",
    "cone-striped",
    "cone",
    "controller",
    "cpu-fill",
    "cpu",
    "credit-card-2-back-fill",
    "credit-card-2-back",
    "credit-card-2-front-fill",
    "credit-card-2-front",
    "credit-card-fill",
    "credit-card",
    "crop",
    "cup-fill",
    "cup-straw",
    "cup",
    "currency-bitcoin",
    "currency-dollar",
    "currency-euro",
    "currency-exchange",
    "currency-pound",
    "currency-yen",
    "cursor-fill",
    "cursor",
    "cursor-text",
    "dash-circle-dotted",
    "dash-circle-fill",
    "dash-circle",
    "dash-lg",
    "dash-square-dotted",
    "dash-square-fill",
    "dash-square",
    "dash",
    "device-hdd-fill",
    "device-hdd",
    "device-ssd-fill",
    "device-ssd",
    "diagram-2-fill",
    "diagram-2",
    "diagram-3-fill",
    "diagram-3",
    "diamond-fill",
    "diamond-half",
    "diamond",
    "dice-1-fill",
    "dice-1",
    "dice-2-fill",
    "dice-2",
    "dice-3-fill",
    "dice-3",
    "dice-4-fill",
    "dice-4",
    "dice-5-fill",
    "dice-5",
    "dice-6-fill",
    "dice-6",
    "disc-fill",
    "discord",
    "disc",
    "display-fill",
    "displayport-fill",
    "displayport",
    "display",
    "distribute-horizontal",
    "distribute-vertical",
    "door-closed-fill",
    "door-closed",
    "door-open-fill",
    "door-open",
    "dot",
    "download",
    "dpad-fill",
    "dpad",
    "dribbble",
    "droplet-fill",
    "droplet-half",
    "droplet",
    "earbuds",
    "ear-fill",
    "ear",
    "easel2-fill",
    "easel2",
    "easel3-fill",
    "easel3",
    "easel-fill",
    "easel",
    "egg-fill",
    "egg-fried",
    "egg",
    "eject-fill",
    "eject",
    "emoji-angry-fill",
    "emoji-angry",
    "emoji-dizzy-fill",
    "emoji-dizzy",
    "emoji-expressionless-fill",
    "emoji-expressionless",
    "emoji-frown-fill",
    "emoji-frown",
    "emoji-heart-eyes-fill",
    "emoji-heart-eyes",
    "emoji-laughing-fill",
    "emoji-laughing",
    "emoji-neutral-fill",
    "emoji-neutral",
    "emoji-smile-fill",
    "emoji-smile",
    "emoji-smile-upside-down-fill",
    "emoji-smile-upside-down",
    "emoji-sunglasses-fill",
    "emoji-sunglasses",
    "emoji-wink-fill",
    "emoji-wink",
    "envelope-check-fill",
    "envelope-check",
    "envelope-dash-fill",
    "envelope-dash",
    "envelope-exclamation-fill",
    "envelope-exclamation",
    "envelope-fill",
    "envelope-open-fill",
    "envelope-open",
    "envelope-plus-fill",
    "envelope-plus",
    "envelope-slash-fill",
    "envelope-slash",
    "envelope",
    "envelope-x-fill",
    "envelope-x",
    "eraser-fill",
    "eraser",
    "ethernet",
    "exclamation-circle-fill",
    "exclamation-circle",
    "exclamation-diamond-fill",
    "exclamation-diamond",
    "exclamation-lg",
    "exclamation-octagon-fill",
    "exclamation-octagon",
    "exclamation-square-fill",
    "exclamation-square",
    "exclamation",
    "exclamation-triangle-fill",
    "exclamation-triangle",
    "exclude",
    "explicit-fill",
    "explicit",
    "eyedropper",
    "eye-fill",
    "eyeglasses",
    "eye-slash-fill",
    "eye-slash",
    "eye",
    "facebook",
    "fan",
    "file-arrow-down-fill",
    "file-arrow-down",
    "file-arrow-up-fill",
    "file-arrow-up",
    "file-bar-graph-fill",
    "file-bar-graph",
    "file-binary-fill",
    "file-binary",
    "file-break-fill",
    "file-break",
    "file-check-fill",
    "file-check",
    "file-code-fill",
    "file-code",
    "file-diff-fill",
    "file-diff",
    "file-earmark-arrow-down-fill",
    "file-earmark-arrow-down",
    "file-earmark-arrow-up-fill",
    "file-earmark-arrow-up",
    "file-earmark-bar-graph-fill",
    "file-earmark-bar-graph",
    "file-earmark-binary-fill",
    "file-earmark-binary",
    "file-earmark-break-fill",
    "file-earmark-break",
    "file-earmark-check-fill",
    "file-earmark-check",
    "file-earmark-code-fill",
    "file-earmark-code",
    "file-earmark-diff-fill",
    "file-earmark-diff",
    "file-earmark-easel-fill",
    "file-earmark-easel",
    "file-earmark-excel-fill",
    "file-earmark-excel",
    "file-earmark-fill",
    "file-earmark-font-fill",
    "file-earmark-font",
    "file-earmark-image-fill",
    "file-earmark-image",
    "file-earmark-lock2-fill",
    "file-earmark-lock2",
    "file-earmark-lock-fill",
    "file-earmark-lock",
    "file-earmark-medical-fill",
    "file-earmark-medical",
    "file-earmark-minus-fill",
    "file-earmark-minus",
    "file-earmark-music-fill",
    "file-earmark-music",
    "file-earmark-pdf-fill",
    "file-earmark-pdf",
    "file-earmark-person-fill",
    "file-earmark-person",
    "file-earmark-play-fill",
    "file-earmark-play",
    "file-earmark-plus-fill",
    "file-earmark-plus",
    "file-earmark-post-fill",
    "file-earmark-post",
    "file-earmark-ppt-fill",
    "file-earmark-ppt",
    "file-earmark-richtext-fill",
    "file-earmark-richtext",
    "file-earmark-ruled-fill",
    "file-earmark-ruled",
    "file-earmark-slides-fill",
    "file-earmark-slides",
    "file-earmark-spreadsheet-fill",
    "file-earmark-spreadsheet",
    "file-earmark",
    "file-earmark-text-fill",
    "file-earmark-text",
    "file-earmark-word-fill",
    "file-earmark-word",
    "file-earmark-x-fill",
    "file-earmark-x",
    "file-earmark-zip-fill",
    "file-earmark-zip",
    "file-easel-fill",
    "file-easel",
    "file-excel-fill",
    "file-excel",
    "file-fill",
    "file-font-fill",
    "file-font",
    "file-image-fill",
    "file-image",
    "file-lock2-fill",
    "file-lock2",
    "file-lock-fill",
    "file-lock",
    "file-medical-fill",
    "file-medical",
    "file-minus-fill",
    "file-minus",
    "file-music-fill",
    "file-music",
    "file-pdf-fill",
    "file-pdf",
    "file-person-fill",
    "file-person",
    "file-play-fill",
    "file-play",
    "file-plus-fill",
    "file-plus",
    "file-post-fill",
    "file-post",
    "file-ppt-fill",
    "file-ppt",
    "file-richtext-fill",
    "file-richtext",
    "file-ruled-fill",
    "file-ruled",
    "files-alt",
    "file-slides-fill",
    "file-slides",
    "file-spreadsheet-fill",
    "file-spreadsheet",
    "files",
    "file",
    "file-text-fill",
    "file-text",
    "file-word-fill",
    "file-word",
    "file-x-fill",
    "file-x",
    "file-zip-fill",
    "file-zip",
    "film",
    "filter-circle-fill",
    "filter-circle",
    "filter-left",
    "filter-right",
    "filter-square-fill",
    "filter-square",
    "filter",
    "fingerprint",
    "flag-fill",
    "flag",
    "flower1",
    "flower2",
    "flower3",
    "folder2-open",
    "folder2",
    "folder-check",
    "folder-fill",
    "folder-minus",
    "folder-plus",
    "folder",
    "folder-symlink-fill",
    "folder-symlink",
    "folder-x",
    "fonts",
    "forward-fill",
    "forward",
    "front",
    "fullscreen-exit",
    "fullscreen",
    "funnel-fill",
    "funnel",
    "gear-fill",
    "gear",
    "gear-wide-connected",
    "gear-wide",
    "gem",
    "gender-ambiguous",
    "gender-female",
    "gender-male",
    "gender-trans",
    "geo-alt-fill",
    "geo-alt",
    "geo-fill",
    "geo",
    "gift-fill",
    "gift",
    "github",
    "git",
    "globe2",
    "globe",
    "google",
    "gpu-card",
    "graph-down-arrow",
    "graph-down",
    "graph-up-arrow",
    "graph-up",
    "grid-1x2-fill",
    "grid-1x2",
    "grid-3x2-gap-fill",
    "grid-3x2-gap",
    "grid-3x2",
    "grid-3x3-gap-fill",
    "grid-3x3-gap",
    "grid-3x3",
    "grid-fill",
    "grid",
    "grip-horizontal",
    "grip-vertical",
    "hammer",
    "handbag-fill",
    "handbag",
    "hand-index-fill",
    "hand-index",
    "hand-index-thumb-fill",
    "hand-index-thumb",
    "hand-thumbs-down-fill",
    "hand-thumbs-down",
    "hand-thumbs-up-fill",
    "hand-thumbs-up",
    "hash",
    "hdd-fill",
    "hdd-network-fill",
    "hdd-network",
    "hdd-rack-fill",
    "hdd-rack",
    "hdd-stack-fill",
    "hdd-stack",
    "hdd",
    "hdmi-fill",
    "hdmi",
    "headphones",
    "headset",
    "headset-vr",
    "heart-fill",
    "heart-half",
    "heart",
    "heptagon-fill",
    "heptagon-half",
    "heptagon",
    "hexagon-fill",
    "hexagon-half",
    "hexagon",
    "hourglass-bottom",
    "hourglass-split",
    "hourglass",
    "hourglass-top",
    "house-door-fill",
    "house-door",
    "house-fill",
    "house",
    "hr",
    "hurricane",
    "hypnotize",
    "image-alt",
    "image-fill",
    "images",
    "image",
    "inboxes-fill",
    "inboxes",
    "inbox-fill",
    "inbox",
    "infinity",
    "info-circle-fill",
    "info-circle",
    "info-lg",
    "info-square-fill",
    "info-square",
    "info",
    "input-cursor",
    "input-cursor-text",
    "instagram",
    "intersect",
    "journal-album",
    "journal-arrow-down",
    "journal-arrow-up",
    "journal-bookmark-fill",
    "journal-bookmark",
    "journal-check",
    "journal-code",
    "journal-medical",
    "journal-minus",
    "journal-plus",
    "journal-richtext",
    "journals",
    "journal",
    "journal-text",
    "journal-x",
    "joystick",
    "justify-left",
    "justify-right",
    "justify",
    "kanban-fill",
    "kanban",
    "keyboard-fill",
    "keyboard",
    "key-fill",
    "key",
    "ladder",
    "lamp-fill",
    "lamp",
    "laptop-fill",
    "laptop",
    "layer-backward",
    "layer-forward",
    "layers-fill",
    "layers-half",
    "layers",
    "layout-sidebar-inset-reverse",
    "layout-sidebar-inset",
    "layout-sidebar-reverse",
    "layout-sidebar",
    "layout-split",
    "layout-text-sidebar-reverse",
    "layout-text-sidebar",
    "layout-text-window-reverse",
    "layout-text-window",
    "layout-three-columns",
    "layout-wtf",
    "life-preserver",
    "lightbulb-fill",
    "lightbulb-off-fill",
    "lightbulb-off",
    "lightbulb",
    "lightning-charge-fill",
    "lightning-charge",
    "lightning-fill",
    "lightning",
    "line",
    "link-45deg",
    "linkedin",
    "link",
    "list-check",
    "list-columns-reverse",
    "list-columns",
    "list-nested",
    "list-ol",
    "list-stars",
    "list",
    "list-task",
    "list-ul",
    "lock-fill",
    "lock",
    "magic",
    "mailbox2",
    "mailbox",
    "map-fill",
    "map",
    "markdown-fill",
    "markdown",
    "mask",
    "mastodon",
    "medium",
    "megaphone-fill",
    "megaphone",
    "memory",
    "menu-app-fill",
    "menu-app",
    "menu-button-fill",
    "menu-button",
    "menu-button-wide-fill",
    "menu-button-wide",
    "menu-down",
    "menu-up",
    "messenger",
    "meta",
    "mic-fill",
    "mic-mute-fill",
    "mic-mute",
    "microsoft",
    "mic",
    "minecart-loaded",
    "minecart",
    "modem-fill",
    "modem",
    "moisture",
    "moon-fill",
    "moon-stars-fill",
    "moon-stars",
    "moon",
    "mortarboard-fill",
    "mortarboard",
    "motherboard-fill",
    "motherboard",
    "mouse2-fill",
    "mouse2",
    "mouse3-fill",
    "mouse3",
    "mouse-fill",
    "mouse",
    "music-note-beamed",
    "music-note-list",
    "music-note",
    "music-player-fill",
    "music-player",
    "newspaper",
    "nintendo-switch",
    "node-minus-fill",
    "node-minus",
    "node-plus-fill",
    "node-plus",
    "nut-fill",
    "nut",
    "octagon-fill",
    "octagon-half",
    "octagon",
    "optical-audio-fill",
    "optical-audio",
    "option",
    "outlet",
    "paint-bucket",
    "palette2",
    "palette-fill",
    "palette",
    "paperclip",
    "paragraph",
    "patch-check-fill",
    "patch-check",
    "patch-exclamation-fill",
    "patch-exclamation",
    "patch-minus-fill",
    "patch-minus",
    "patch-plus-fill",
    "patch-plus",
    "patch-question-fill",
    "patch-question",
    "pause-btn-fill",
    "pause-btn",
    "pause-circle-fill",
    "pause-circle",
    "pause-fill",
    "pause",
    "paypal",
    "pc-display-horizontal",
    "pc-display",
    "pc-horizontal",
    "pci-card",
    "pc",
    "peace-fill",
    "peace",
    "pencil-fill",
    "pencil-square",
    "pencil",
    "pen-fill",
    "pen",
    "pentagon-fill",
    "pentagon-half",
    "pentagon",
    "people-fill",
    "people",
    "percent",
    "person-badge-fill",
    "person-badge",
    "person-bounding-box",
    "person-check-fill",
    "person-check",
    "person-circle",
    "person-dash-fill",
    "person-dash",
    "person-fill",
    "person-lines-fill",
    "person-plus-fill",
    "person-plus",
    "person-rolodex",
    "person-square",
    "person",
    "person-video2",
    "person-video3",
    "person-video",
    "person-workspace",
    "person-x-fill",
    "person-x",
    "phone-fill",
    "phone-landscape-fill",
    "phone-landscape",
    "phone",
    "phone-vibrate-fill",
    "phone-vibrate",
    "pie-chart-fill",
    "pie-chart",
    "piggy-bank-fill",
    "piggy-bank",
    "pin-angle-fill",
    "pin-angle",
    "pin-fill",
    "pin-map-fill",
    "pin-map",
    "pin",
    "pinterest",
    "pip-fill",
    "pip",
    "play-btn-fill",
    "play-btn",
    "play-circle-fill",
    "play-circle",
    "play-fill",
    "playstation",
    "play",
    "plug-fill",
    "plug",
    "plus-circle-dotted",
    "plus-circle-fill",
    "plus-circle",
    "plus-lg",
    "plus-slash-minus",
    "plus-square-dotted",
    "plus-square-fill",
    "plus-square",
    "plus",
    "power",
    "printer-fill",
    "printer",
    "projector-fill",
    "projector",
    "puzzle-fill",
    "puzzle",
    "qr-code-scan",
    "qr-code",
    "question-circle-fill",
    "question-circle",
    "question-diamond-fill",
    "question-diamond",
    "question-lg",
    "question-octagon-fill",
    "question-octagon",
    "question-square-fill",
    "question-square",
    "question",
    "quora",
    "quote",
    "radioactive",
    "rainbow",
    "receipt-cutoff",
    "receipt",
    "reception-0",
    "reception-1",
    "reception-2",
    "reception-3",
    "reception-4",
    "record2-fill",
    "record2",
    "record-btn-fill",
    "record-btn",
    "record-circle-fill",
    "record-circle",
    "record-fill",
    "record",
    "recycle",
    "reddit",
    "reply-all-fill",
    "reply-all",
    "reply-fill",
    "reply",
    "robot",
    "router-fill",
    "router",
    "rss-fill",
    "rss",
    "rulers",
    "safe2-fill",
    "safe2",
    "safe-fill",
    "safe",
    "save2-fill",
    "save2",
    "save-fill",
    "save",
    "scissors",
    "screwdriver",
    "sd-card-fill",
    "sd-card",
    "search",
    "segmented-nav",
    "send-check-fill",
    "send-check",
    "send-dash-fill",
    "send-dash",
    "send-exclamation-fill",
    "send-exclamation",
    "send-fill",
    "send-plus-fill",
    "send-plus",
    "send-slash-fill",
    "send-slash",
    "send",
    "send-x-fill",
    "send-x",
    "server",
    "share-fill",
    "share",
    "shield-check",
    "shield-exclamation",
    "shield-fill-check",
    "shield-fill-exclamation",
    "shield-fill-minus",
    "shield-fill-plus",
    "shield-fill",
    "shield-fill-x",
    "shield-lock-fill",
    "shield-lock",
    "shield-minus",
    "shield-plus",
    "shield-shaded",
    "shield-slash-fill",
    "shield-slash",
    "shield",
    "shield-x",
    "shift-fill",
    "shift",
    "shop",
    "shop-window",
    "shuffle",
    "signal",
    "signpost-2-fill",
    "signpost-2",
    "signpost-fill",
    "signpost-split-fill",
    "signpost-split",
    "signpost",
    "sim-fill",
    "sim",
    "skip-backward-btn-fill",
    "skip-backward-btn",
    "skip-backward-circle-fill",
    "skip-backward-circle",
    "skip-backward-fill",
    "skip-backward",
    "skip-end-btn-fill",
    "skip-end-btn",
    "skip-end-circle-fill",
    "skip-end-circle",
    "skip-end-fill",
    "skip-end",
    "skip-forward-btn-fill",
    "skip-forward-btn",
    "skip-forward-circle-fill",
    "skip-forward-circle",
    "skip-forward-fill",
    "skip-forward",
    "skip-start-btn-fill",
    "skip-start-btn",
    "skip-start-circle-fill",
    "skip-start-circle",
    "skip-start-fill",
    "skip-start",
    "skype",
    "slack",
    "slash-circle-fill",
    "slash-circle",
    "slash-lg",
    "slash-square-fill",
    "slash-square",
    "slash",
    "sliders",
    "smartwatch",
    "snapchat",
    "snow2",
    "snow3",
    "snow",
    "sort-alpha-down-alt",
    "sort-alpha-down",
    "sort-alpha-up-alt",
    "sort-alpha-up",
    "sort-down-alt",
    "sort-down",
    "sort-numeric-down-alt",
    "sort-numeric-down",
    "sort-numeric-up-alt",
    "sort-numeric-up",
    "sort-up-alt",
    "sort-up",
    "soundwave",
    "speaker-fill",
    "speaker",
    "speedometer2",
    "speedometer",
    "spellcheck",
    "spotify",
    "square-fill",
    "square-half",
    "square",
    "stack-overflow",
    "stack",
    "star-fill",
    "star-half",
    "stars",
    "star",
    "steam",
    "stickies-fill",
    "stickies",
    "sticky-fill",
    "sticky",
    "stop-btn-fill",
    "stop-btn",
    "stop-circle-fill",
    "stop-circle",
    "stop-fill",
    "stoplights-fill",
    "stoplights",
    "stop",
    "stopwatch-fill",
    "stopwatch",
    "strava",
    "subtract",
    "suit-club-fill",
    "suit-club",
    "suit-diamond-fill",
    "suit-diamond",
    "suit-heart-fill",
    "suit-heart",
    "suit-spade-fill",
    "suit-spade",
    "sun-fill",
    "sunglasses",
    "sunrise-fill",
    "sunrise",
    "sunset-fill",
    "sunset",
    "sun",
    "symmetry-horizontal",
    "symmetry-vertical",
    "table",
    "tablet-fill",
    "tablet-landscape-fill",
    "tablet-landscape",
    "tablet",
    "tag-fill",
    "tags-fill",
    "tags",
    "tag",
    "telegram",
    "telephone-fill",
    "telephone-forward-fill",
    "telephone-forward",
    "telephone-inbound-fill",
    "telephone-inbound",
    "telephone-minus-fill",
    "telephone-minus",
    "telephone-outbound-fill",
    "telephone-outbound",
    "telephone-plus-fill",
    "telephone-plus",
    "telephone",
    "telephone-x-fill",
    "telephone-x",
    "terminal-dash",
    "terminal-fill",
    "terminal-plus",
    "terminal-split",
    "terminal",
    "terminal-x",
    "textarea-resize",
    "textarea",
    "textarea-t",
    "text-center",
    "text-indent-left",
    "text-indent-right",
    "text-left",
    "text-paragraph",
    "text-right",
    "thermometer-half",
    "thermometer-high",
    "thermometer-low",
    "thermometer-snow",
    "thermometer-sun",
    "thermometer",
    "three-dots",
    "three-dots-vertical",
    "thunderbolt-fill",
    "thunderbolt",
    "ticket-detailed-fill",
    "ticket-detailed",
    "ticket-fill",
    "ticket-perforated-fill",
    "ticket-perforated",
    "ticket",
    "tiktok",
    "toggle2-off",
    "toggle2-on",
    "toggle-off",
    "toggle-on",
    "toggles2",
    "toggles",
    "tools",
    "tornado",
    "translate",
    "trash2-fill",
    "trash2",
    "trash-fill",
    "trash",
    "tree-fill",
    "tree",
    "triangle-fill",
    "triangle-half",
    "triangle",
    "trophy-fill",
    "trophy",
    "tropical-storm",
    "truck-flatbed",
    "truck",
    "tsunami",
    "tv-fill",
    "tv",
    "twitch",
    "twitter",
    "type-bold",
    "type-h1",
    "type-h2",
    "type-h3",
    "type-italic",
    "type-strikethrough",
    "type",
    "type-underline",
    "ui-checks-grid",
    "ui-checks",
    "ui-radios-grid",
    "ui-radios",
    "umbrella-fill",
    "umbrella",
    "union",
    "unlock-fill",
    "unlock",
    "upc-scan",
    "upc",
    "upload",
    "usb-c-fill",
    "usb-c",
    "usb-drive-fill",
    "usb-drive",
    "usb-fill",
    "usb-micro-fill",
    "usb-micro",
    "usb-mini-fill",
    "usb-mini",
    "usb-plug-fill",
    "usb-plug",
    "usb",
    "usb-symbol",
    "vector-pen",
    "view-list",
    "view-stacked",
    "vimeo",
    "vinyl-fill",
    "vinyl",
    "voicemail",
    "volume-down-fill",
    "volume-down",
    "volume-mute-fill",
    "volume-mute",
    "volume-off-fill",
    "volume-off",
    "volume-up-fill",
    "volume-up",
    "vr",
    "wallet2",
    "wallet-fill",
    "wallet",
    "watch",
    "water",
    "webcam-fill",
    "webcam",
    "whatsapp",
    "wifi-1",
    "wifi-2",
    "wifi-off",
    "wifi",
    "window-dash",
    "window-desktop",
    "window-dock",
    "window-fullscreen",
    "window-plus",
    "window-sidebar",
    "window-split",
    "windows",
    "window-stack",
    "window",
    "window-x",
    "wind",
    "wordpress",
    "wrench",
    "xbox",
    "x-circle-fill",
    "x-circle",
    "x-diamond-fill",
    "x-diamond",
    "x-lg",
    "x-octagon-fill",
    "x-octagon",
    "x-square-fill",
    "x-square",
    "x",
    "yin-yang",
    "youtube",
    "zoom-in",
    "zoom-out",
]
db.drop_all()
db.create_all()
for i in range(10):
    listing = Listing(
        title=get_word(count=10),
        price=random.randrange(100, 1000),
        slug=nanoid.generate(
            "1234567890abcdefghijklmnopqrtsuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ", size=6
        ),
        image="/static/pic.jpg",
        shortDescription=get_sentence(count=2),
        dimension=random.randrange(0, 100),
        city=fake.city(),
        street=fake.address(),
        startDate=fake.date_time(),
        endDate=fake.date_time(),
        icon="bi-" + random.choice(icons),
        color=random.choice(wes),
    )
    db.session.add(listing)
db.session.commit()
