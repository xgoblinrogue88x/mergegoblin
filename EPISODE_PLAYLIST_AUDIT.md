# Numbered episode playlist audit

**Source:** the user-supplied YouTube channel listing and catalog.json export. This audits every numbered episode playlist in that snapshot; it is not a claim of a fresh live YouTube visit. Live access is pending activation of the environment network allowlist change.

The channel's `#number` playlists define individual episodes. Artist-only playlists and `Episodes X - Y` collections are excluded from episode discovery.

- 88 distinct numbered episode playlists in the range E01–E91.
- 766 playlist entries, representing 759 unique YouTube video IDs.
- E02, E13 and E29 are absent from this snapshot. The user confirmed E02 is intentionally missing; no cause is asserted for any missing playlist.
- E07 repeats video N1zpSaNHK10 (Foolish Pride) twice. Keep its first occurrence for the merge; this produces 8 unique clips.
- Six video IDs appear in both an original episode and E32. These are legitimate shared playlist references, not evidence that two files are needed.
- Eli Reed's Pick A Number has identical titles but different IDs in E27 and E32. A filename alone cannot identify which upload was downloaded.
- No missing video IDs or explicitly unavailable/private/deleted placeholder titles were found. YouTube may omit unavailable items from a listing, so this does not establish broadcast completeness.
- The separate Episodes 1–10 export contains 76 unique videos. Its IDs and order match E01 and E03–E10 after removing E07's duplicate.

## Playlist index

| Episode | Playlist title | Entries | Unique videos |
|---|---|---:|---:|
| E01 | [#1 - Daryl Hall - The Debut Episode of Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfFgbUX1dfhp4rYn-780Qsu) | 8 | 8 |
| E03 | [#3 - Daryl Hall on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdehN04KOurSVxTmSlAYOiK) | 8 | 8 |
| E04 | [#4 - Daryl Hall hosts Travis McCoy on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdCPvIUiH-K5ECj0LdRRBEr) | 10 | 10 |
| E05 | [#5 - Daryl Hall hosts KT Tunstall on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdwEaFAmZe0kBWmBhme7b6i) | 10 | 10 |
| E06 | [#6 - Daryl Hall Performs Live at SXSW](https://www.youtube.com/playlist?list=PLINSQGXREtvcy_OtGPnm--lwQDFTTljg-) | 6 | 6 |
| E07 | [#7 - Daryl Hall hosts Mutlu &amp; Chuck Prophet on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdm0FCMWSNKYl3blDhH0Yw5) | 9 | 8 |
| E08 | [#8 - Daryl Hall hosts Nick Lowe on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveHWyTBiIcA_d5K1Tdl2f4q) | 8 | 8 |
| E09 | [#9 - Daryl Hall hosts Monte Montgomery on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc_n32YOAgp748VrRJULdPy) | 8 | 8 |
| E10 | [#10 - Daryl Hall hosts Chromeo on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveEcVjY6caUTMQ3BEJQJ5rC) | 10 | 10 |
| E11 | [#11 - Daryl Hall hosts Finger Eleven on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdhH5L9tu_yPt4VRzRZjVsN) | 10 | 10 |
| E12 | [#12 - Daryl Hall hosts Eric Hutchinson on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdu1jLkyBOxVen5sAGSzOo-) | 10 | 10 |
| E14 | [#14 - Daryl Hall hosts Kevin Rudolf on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdGhsk543B0rZQUOiQ3V31s) | 10 | 10 |
| E15 | [#15 - Daryl Hall hosts Company Of Thieves on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdkj1zJsPh_hVKXRyEfxMQM) | 8 | 8 |
| E16 | [#16 - Daryl Hall hosts The Bacon Brothers on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc28o-RIKn9gy-OQRV--fa9) | 10 | 10 |
| E17 | [#17 - Daryl Hall hosts Matt Nathanson on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcU64m47bOrrou818Vg87ZW) | 8 | 8 |
| E18 | [#18 - Daryl Hall hosts Robby Krieger and Ray Manzarek of The Doors on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc52PZ0NFqoM2IGlUwXvX18) | 7 | 7 |
| E19 | [#19 - Retrospective](https://www.youtube.com/playlist?list=PLINSQGXREtvfbCL6Mly4EKIAPdHWKh5aX) | 6 | 6 |
| E20 | [#20 - Daryl Hall hosts Parachute on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveSxwUP0sJlr41uTr_XDmKM) | 7 | 7 |
| E21 | [#21 - Daryl Hall hosts Plain White T&#x27;s on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcV2uzbeuPJL-4lj_elLw2M) | 8 | 8 |
| E22 | [#22 - Daryl Hall hosts Smokey Robinson on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcZBYfgAB-yMv_7DtIaULIp) | 9 | 9 |
| E23 | [#23 - Daryl Hall hosts Todd Rundgren on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtve4nqpvEEXKmBk1iAik0Iiq) | 10 | 10 |
| E24 | [#24 - Daryl Hall hosts Diane Birch on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveKou9G_zF_acHO6KhSF1nt) | 8 | 8 |
| E25 | [#25 - Daryl Hall hosts Patrick Stump of Fall Out Boy on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfJQa7dQsB7CDg8Q8Jig7Xp) | 8 | 8 |
| E26 | [#26 - Daryl Hall hosts Jimmy Wayne on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveF-xh0wO8eIBknD0e2eZoO) | 7 | 7 |
| E27 | [#27 - Daryl Hall hosts Eli &quot;Paperboy&quot; Reed on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdj1ypoRkQgXKDOL7sbK7uJ) | 10 | 10 |
| E28 | [#28 - Daryl Hall hosts Toots &amp; The Maytals on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfsNIhj9QGMcSyRvbGO_NQc) | 8 | 8 |
| E30 | [#30 - Daryl Hall&#x27;s Tribute to T-Bone](https://www.youtube.com/playlist?list=PLINSQGXREtvflWAdBuyAKxYLXsA8OZYZu) | 15 | 15 |
| E31 | [#31 - Daryl Hall hosts Rob Thomas of Matchbox 20 on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdzf55J_NPZDRn1rtMLhHbI) | 8 | 8 |
| E32 | [#32 - Daryl Hall&#x27;s Retrospective 2 on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveA99ijYCJc744xX7GHJi_m) | 14 | 14 |
| E33 | [#33 - Daryl Hall hosts Pat Monahan of Train on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvf9i892uSlIfyHQFdAVnw3K) | 8 | 8 |
| E34 | [#34 - Daryl Hall hosts Sharon Jones on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvciVmXkb3zq5hyCnswL9mwJ) | 9 | 9 |
| E35 | [#35 - Daryl Hall hosts Fitz and The Tantrums on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtve85S8RDwWJy0IJtaqmcHa7) | 9 | 9 |
| E36 | [#36 - Daryl Hall hosts Neon Trees on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdkAGixSfTYLyjegbJWJw8L) | 9 | 9 |
| E37 | [#37 - Daryl Hall hosts Jose Feliciano on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveB3_ynDKJMEEka-0zaDVUM) | 9 | 9 |
| E38 | [#38 - Daryl Hall hosts Guster on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdJF6zcVcWiJRi191HYtoXI) | 8 | 8 |
| E39 | [#39 - New Years Eve Special on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveyLJaQUV5Zvzxffg5YpJ8C) | 12 | 12 |
| E40 | [#40 - Daryl Hall hosts Todd Rundgren on Live From Daryl&#x27;s House in Hawaii](https://www.youtube.com/playlist?list=PLINSQGXREtvckRDkC3dG4f-EVTHfa041G) | 10 | 10 |
| E41 | [#41 - Daryl Hall hosts Dave Stewart of Eurythmics on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcx4eZQXJFedgzZTUAZ7SwF) | 9 | 9 |
| E42 | [#42 - Daryl Hall hosts John Rzeznik of Goo Goo Dolls on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvczXcIq4QePBkvLUC85agfG) | 8 | 8 |
| E43 | [#43 - Daryl Hall hosts Mayer Hawthorne on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcYMNrWP1AN0JQ4gYblg2KW) | 8 | 8 |
| E44 | [#44 - Daryl Hall hosts Booker T. Jones on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvf6asN95rllRtPTDms4Cu1K) | 8 | 8 |
| E45 | [#45 - Daryl Hall hosts Grace Potter on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfKbU3sg39y2E0c6xYGi3XQ) | 8 | 8 |
| E46 | [#46 - Daryl Hall hosts Nikki Jean on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc5X_Jj8lTmhW_iWJX8KD-b) | 14 | 14 |
| E47 | [#47 - Daryl Hall Performs &quot;Laughing Down Crying&quot; Part 1](https://www.youtube.com/playlist?list=PLINSQGXREtvdPi8LsxG2rQOOzL_VCOf8z) | 7 | 7 |
| E48 | [#48 - Daryl Hall Performs &quot;Laughing Down Crying&quot; Part 2](https://www.youtube.com/playlist?list=PLINSQGXREtvdUY8ofO6Ig5GvG2uiYKFFJ) | 7 | 7 |
| E49 | [#49 - Daryl Hall hosts Blind Boys of Alabama on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdrLNdNtIHPYYST1kh7M3fJ) | 8 | 8 |
| E50 | [#50 - Daryl Hall hosts Keb&#x27; Mo&#x27; on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveU9ewvOExoXNvdMWPo83NV) | 9 | 9 |
| E51 | [#51 - Daryl Hall hosts Allen Stone on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdxN7Zp-TbPiN6jTECbXWP8) | 13 | 13 |
| E52 | [#52 - Daryl Hall hosts CeeLo Green on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfY1kC4iUXLirBbTpvGOzaC) | 9 | 9 |
| E53 | [#53 - Daryl Hall hosts Dirty Heads on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvekHd-GuiByzm25w7KK1jwJ) | 11 | 11 |
| E54 | [#54 - Daryl Hall hosts Butch Walker on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcLROJJSnX996n6gMP1-u4x) | 12 | 12 |
| E55 | [#55 - Daryl Hall hosts Jason Mraz on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfZILRE6ej6ZuXMpJe30Dvg) | 7 | 7 |
| E56 | [#56 - Daryl Hall hosts Chiddy Bang on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvehk-2P6RK0nJRREH3joeVc) | 8 | 8 |
| E57 | [#57 - Daryl Hall hosts Rumer on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdpFq6iW-3VIcibf3g4rc13) | 7 | 7 |
| E58 | [#58 - Daryl Hall hosts Nick Waterhouse on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtve9BIHu6qezOsN_64UNYcP9) | 8 | 8 |
| E59 | [#59 - Daryl Hall hosts Soul Revue on Live From Daryl&#x27;s House (Live at The Borgata)](https://www.youtube.com/playlist?list=PLINSQGXREtve2lAswaqi5WGGTiiHnZr9e) | 8 | 8 |
| E60 | [#60 - Daryl Hall hosts Joe Walsh of The Eagles on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcibYqcUBQEqieNEOicj_Kq) | 8 | 8 |
| E61 | [#61 - Daryl Hall hosts Shelby Lynne on Live From Daryl&#x27;s House for Christmas](https://www.youtube.com/playlist?list=PLINSQGXREtvf96l9SWRj9J42IFuOMJ9bw) | 8 | 8 |
| E62 | [#62 - Daryl Hall hosts Minus The Bear on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfTgobdsq9Gf34CCp_rinTt) | 8 | 8 |
| E63 | [#63 - Daryl Hall hosts Billy Gibbons of ZZ Top on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc7ZbsRTfXlnFda6isz7DEw) | 9 | 9 |
| E64 | [#64 - Daryl Hall hosts Gavin DeGraw on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvegRkdfTBQwfw4P86Gu-E90) | 7 | 7 |
| E65 | [#65 - Daryl Hall hosts Johnnyswim on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdyuRWmLMSZnvzmJ1816LDs) | 8 | 8 |
| E66 | [#66 - Daryl Hall hosts Amos Lee on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvfdTOPXPnxtxjnqFzZIHSnY) | 9 | 9 |
| E67 | [#67 - Daryl Hall hosts Brett Dennen on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdNa0zGRSsbCgrv3cNwD6Q2) | 8 | 8 |
| E68 | [#68 - Daryl Hall hosts Darius Rucker of Hootie and The Blowfish on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvem3gWthZrEuRXHD0MhFsHL) | 9 | 9 |
| E69 | [#69 - Daryl Hall hosts Sammy Hagar on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdhiQOPB9Zccn7zxa5Bp5ex) | 8 | 8 |
| E70 | [#70 - Daryl Hall hosts Ben Folds on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveWPM6DI4AutJ6Zptu_4EgQ) | 8 | 8 |
| E71 | [#71 - Daryl Hall hosts Kandace Springs on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveY6b3LJkAQxPGYdRuGYA4P) | 7 | 7 |
| E72 | [#72 - Daryl Hall hosts Aaron Neville on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvc_Qt4Lbo2-cfs4UuF1pLk5) | 9 | 9 |
| E73 | [#73 - Daryl Hall hosts Kitty, Daisy &amp; Lewis on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvchL_s7exmAgmGTx_1S3B94) | 8 | 8 |
| E74 | [#74 - Daryl Hall hosts Aloe Blacc on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvePXFMfab_DXTa46TnSPahk) | 8 | 8 |
| E75 | [#75 - Daryl Hall hosts Cheap Trick on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcKO-0JzfIAdmDM9lKm0tSZ) | 9 | 9 |
| E76 | [#76 - Daryl Hall hosts Wyclef Jean on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvf_rpjlCBU5ekWFlBgpuSrE) | 8 | 8 |
| E77 | [#77 - Daryl Hall hosts Elle King on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvetcPedlyfTCBN6k6FaU3Wj) | 8 | 8 |
| E78 | [#78 - Daryl Hall hosts The O&#x27;Jays on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcy_DleHnvN4DGIK2cvMDpf) | 9 | 9 |
| E79 | [#79 - Daryl Hall hosts Anderson East on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvd73SQQrFNyZkGqNiIxL_7f) | 9 | 9 |
| E80 | [#80 - Daryl Hall hosts Daughtry on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcv_xxFSjjOAfqCDSqZfNjq) | 9 | 9 |
| E81 | [#81 - Daryl Hall hosts SayGrace on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcbqtO9AMAp9yAqagSIRBYv) | 8 | 8 |
| E82 | [#82 - Daryl Hall hosts Kenny Loggins on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvd8drXYA7JUwQP9vMywQFYo) | 9 | 9 |
| E83 | [#83 - Daryl Hall hosts Tommy Shaw of Styx on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcPFDvw_vLiZo5YXDscmflu) | 8 | 8 |
| E84 | [#84 - Daryl Hall hosts Ty Taylor of Vintage Trouble on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdhHIzkScMCGgC6hAimjHTG) | 8 | 8 |
| E85 | [#85 - Daryl Hall hosts Glenn Tilbrook of Squeeze on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvczpZBPRlWqSPMKSOvmX1Er) | 8 | 8 |
| E86 | [#86 - Daryl Hall hosts Charlie Starr of Blackberry Smoke on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcV3Q26wTKxcpzrLnfjNQ4v) | 8 | 8 |
| E87 | [#87 - Daryl Hall hosts Robert Fripp on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdnvCfLXTt0GmE8Oz_8s2tQ) | 8 | 8 |
| E88 | [#88 - Daryl Hall hosts Andy Grammer on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtveW4HQ3qocWr6AEk6xGb7Vv) | 8 | 8 |
| E89 | [#89 - Daryl Hall hosts Lisa Loeb on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcAkWGPYI_jmuRpFpXK5-wc) | 8 | 8 |
| E90 | [#90 - Daryl Hall hosts Howard Jones on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvdQSlQ8xUqyOrdl7mRPUdOE) | 8 | 8 |
| E91 | [#91 - Daryl Hall hosts Dave Stewart &amp; Vanessa Amorosi on Live From Daryl&#x27;s House](https://www.youtube.com/playlist?list=PLINSQGXREtvcwnOwZyKjjpVRw3FDYEYCe) | 10 | 10 |

## Videos shared between episodes

| Video | Episodes | Title |
|---|---|---|
| [tsJ_J5KVKLM](https://www.youtube.com/watch?v=tsJ_J5KVKLM) | E22, E32 | Daryl Hall &amp; Smokey Robinson - Sara Smile / Ooh Baby Baby (Live From Daryl&#x27;s House) |
| [rmRrqBFFVog](https://www.youtube.com/watch?v=rmRrqBFFVog) | E23, E32 | Daryl Hall &amp; Todd Rundgren - The Want Of A Nail (Live From Daryl&#x27;s House) |
| [FPYJUxTOy7s](https://www.youtube.com/watch?v=FPYJUxTOy7s) | E24, E32 | Daryl Hall &amp; Diane Birch - Daydreaming (Live From Daryl&#x27;s House) |
| [uadYC1H0RoY](https://www.youtube.com/watch?v=uadYC1H0RoY) | E26, E32 | Daryl Hall &amp; Jimmy Wayne - Kerosene Kid (Live From Daryl&#x27;s House) |
| [GdKyVQHCtXk](https://www.youtube.com/watch?v=GdKyVQHCtXk) | E28, E32 | Daryl Hall &amp; Toots and the Maytals - Reggae Got Soul (Live From Daryl&#x27;s House) |
| [mvBpknUcO3U](https://www.youtube.com/watch?v=mvBpknUcO3U) | E30, E32 | Tribute to T-Bone - I Miss You (Live From Daryl&#x27;s House) |

## Same-title identity conflict

Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Pick A Number (Live From Daryl&#x27;s House)

- [8Rry_PXRPPY](https://www.youtube.com/watch?v=8Rry_PXRPPY)
- [Vl6gZwnM4hw](https://www.youtube.com/watch?v=Vl6gZwnM4hw)

## Full per-episode clip inventory

Order below is the supplied playlist order. Original playlist indices are shown without guessing an alternative broadcast order.

### E01: #1 - Daryl Hall - The Debut Episode of Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfFgbUX1dfhp4rYn-780Qsu

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [uYa0Zri-v2k](https://www.youtube.com/watch?v=uYa0Zri-v2k) | Daryl Hall - Everything Your Heart Desires (Live From Daryl&#x27;s House - The Debut Episode) |
| 2 | 2 | [s1WqioqlL2M](https://www.youtube.com/watch?v=s1WqioqlL2M) | Daryl Hall - Cab Driver (Live From Daryl&#x27;s House - The Debut Episode) |
| 3 | 3 | [-zvdVeGVUUo](https://www.youtube.com/watch?v=-zvdVeGVUUo) | Daryl Hall - It&#x27;s A Laugh (Live From Daryl&#x27;s House - The Debut Episode) |
| 4 | 4 | [Tmrqz5w2gds](https://www.youtube.com/watch?v=Tmrqz5w2gds) | Daryl Hall - Sara Smile (Live From Daryl&#x27;s House - The Debut Episode) |
| 5 | 5 | [8cJOJ2cFzUM](https://www.youtube.com/watch?v=8cJOJ2cFzUM) | Daryl Hall - Dreamtime (Live From Daryl&#x27;s House - The Debut Episode) |
| 6 | 6 | [-ow9SZVZq5Q](https://www.youtube.com/watch?v=-ow9SZVZq5Q) | Daryl Hall - I&#x27;m In A Philly Mood (Live From Daryl&#x27;s House - The Debut Episode) |
| 7 | 7 | [wfRqVpigdz8](https://www.youtube.com/watch?v=wfRqVpigdz8) | Daryl Hall - Someone Else&#x27;s Kids (Live From Daryl&#x27;s House - The Debut Episode) |
| 8 | 8 | [y-h_eZKb7ls](https://www.youtube.com/watch?v=y-h_eZKb7ls) | Daryl Hall - Foolish Pride (Live From Daryl&#x27;s House - The Debut Episode) |

### E03: #3 - Daryl Hall on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdehN04KOurSVxTmSlAYOiK

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-bMztdLPUS4](https://www.youtube.com/watch?v=-bMztdLPUS4) | Daryl Hall - Rich Girl (Live From Daryl&#x27;s House) |
| 2 | 2 | [RE4lJZGxeSY](https://www.youtube.com/watch?v=RE4lJZGxeSY) | Daryl Hall - You Make My Dreams (Live From Daryl&#x27;s House) |
| 3 | 3 | [mXMyr4_NzRA](https://www.youtube.com/watch?v=mXMyr4_NzRA) | Daryl Hall - Kiss On My List (Live From Daryl&#x27;s House) |
| 4 | 4 | [dtcDtGiSFuo](https://www.youtube.com/watch?v=dtcDtGiSFuo) | Daryl Hall - Someone Else&#x27;s Kids (Live From Daryl&#x27;s House) |
| 5 | 5 | [Zf0YcVUXpwQ](https://www.youtube.com/watch?v=Zf0YcVUXpwQ) | Daryl Hall - Stop Loving Me, Stop Loving You (Live From Daryl&#x27;s House) |
| 6 | 6 | [pXGg8t8yxAI](https://www.youtube.com/watch?v=pXGg8t8yxAI) | Daryl Hall - Somebody Like You (Live From Daryl&#x27;s House) |
| 7 | 7 | [_QPH7a-xduw](https://www.youtube.com/watch?v=_QPH7a-xduw) | Daryl Hall - Maneater (Live From Daryl&#x27;s House) |
| 8 | 8 | [GOVwPBHkO4s](https://www.youtube.com/watch?v=GOVwPBHkO4s) | Daryl Hall - What&#x27;s Gonna Happen To Us (Live From Daryl&#x27;s House) |

### E04: #4 - Daryl Hall hosts Travis McCoy on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdCPvIUiH-K5ECj0LdRRBEr

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [SyC9iBPfVs8](https://www.youtube.com/watch?v=SyC9iBPfVs8) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [3n1k8N75BQU](https://www.youtube.com/watch?v=3n1k8N75BQU) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Uncanny (Live From Daryl&#x27;s House) |
| 3 | 3 | [ffamY3iyb6w](https://www.youtube.com/watch?v=ffamY3iyb6w) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - The Queen &amp; I (Live From Daryl&#x27;s House) |
| 4 | 4 | [hOswmPW4QkU](https://www.youtube.com/watch?v=hOswmPW4QkU) | Daryl Hall &amp; Travis McCoy - Be Thankful For What You Got (Live From Daryl&#x27;s House) |
| 5 | 5 | [LM06WjNjxQI](https://www.youtube.com/watch?v=LM06WjNjxQI) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Can&#x27;t Stop Dreaming (Live From Daryl&#x27;s House) |
| 6 | 6 | [geacjCqftNg](https://www.youtube.com/watch?v=geacjCqftNg) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Wake Up Everybody (Live From Daryl&#x27;s House) |
| 7 | 7 | [fhM2OwOrKeo](https://www.youtube.com/watch?v=fhM2OwOrKeo) | Daryl Hall &amp; Travis McCoy - Don&#x27;t Let Me Be Misunderstood (Live From Daryl&#x27;s House) |
| 8 | 8 | [3EY_NJQVk8Y](https://www.youtube.com/watch?v=3EY_NJQVk8Y) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Everytime You Go Away (Live From Daryl&#x27;s House) |
| 9 | 9 | [MyFS1uGNj6o](https://www.youtube.com/watch?v=MyFS1uGNj6o) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - Valentine (Live From Daryl&#x27;s House) |
| 10 | 10 | [wuprxaQC9sE](https://www.youtube.com/watch?v=wuprxaQC9sE) | Daryl Hall &amp; Travis McCoy (Gym Class Heroes) - End (Live From Daryl&#x27;s House) |

### E05: #5 - Daryl Hall hosts KT Tunstall on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdwEaFAmZe0kBWmBhme7b6i

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-Rj5-n05c3A](https://www.youtube.com/watch?v=-Rj5-n05c3A) | Daryl Hall &amp; KT Tunstall - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [Dhk09eP1HOU](https://www.youtube.com/watch?v=Dhk09eP1HOU) | Daryl Hall &amp; KT Tunstall - Something To Talk About (Live From Daryl&#x27;s House) |
| 3 | 3 | [PVnGyroE3So](https://www.youtube.com/watch?v=PVnGyroE3So) | Daryl Hall &amp; KT Tunstall - If Only (Live From Daryl&#x27;s House) |
| 4 | 4 | [oMrwKz5MT2M](https://www.youtube.com/watch?v=oMrwKz5MT2M) | Daryl Hall &amp; KT Tunstall - Black Horse and The Cherry Tree (Live From Daryl&#x27;s House) |
| 5 | 5 | [hlUcBNNR9R4](https://www.youtube.com/watch?v=hlUcBNNR9R4) | Daryl Hall &amp; KT Tunstall - Kiss On My List (Live From Daryl&#x27;s House) |
| 6 | 6 | [HxbzMPIEzRc](https://www.youtube.com/watch?v=HxbzMPIEzRc) | Daryl Hall &amp; KT Tunstall - Out Of Touch (Live From Daryl&#x27;s House) |
| 7 | 7 | [BhViCTUghng](https://www.youtube.com/watch?v=BhViCTUghng) | Daryl Hall &amp; KT Tunstall - I&#x27;ll Be Around (Live From Daryl&#x27;s House) |
| 8 | 8 | [WTLU5oV5oT8](https://www.youtube.com/watch?v=WTLU5oV5oT8) | Daryl Hall &amp; KT Tunstall - Getaway Car (Live From Daryl&#x27;s House) |
| 9 | 9 | [3x3pzCT5e9A](https://www.youtube.com/watch?v=3x3pzCT5e9A) | Daryl Hall &amp; KT Tunstall - One On One (Live From Daryl&#x27;s House) |
| 10 | 10 | [KdlSMcjdEPw](https://www.youtube.com/watch?v=KdlSMcjdEPw) | Daryl Hall &amp; KT Tunstall - End (Live From Daryl&#x27;s House) |

### E06: #6 - Daryl Hall Performs Live at SXSW

https://www.youtube.com/playlist?list=PLINSQGXREtvcy_OtGPnm--lwQDFTTljg-

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [5HzXItpZBY0](https://www.youtube.com/watch?v=5HzXItpZBY0) | Daryl Hall - You Make My Dreams (Live at SXSW) |
| 2 | 2 | [pthGZeB8kJs](https://www.youtube.com/watch?v=pthGZeB8kJs) | Daryl Hall - Everything Your Heart Desires (Live at SXSW) |
| 3 | 3 | [ScIeTEV_SK4](https://www.youtube.com/watch?v=ScIeTEV_SK4) | Daryl Hall - Cab Driver (Live at SXSW) |
| 4 | 4 | [-ACiRFrGW7o](https://www.youtube.com/watch?v=-ACiRFrGW7o) | Daryl Hall - I Can&#x27;t Stop Dreaming (Live at SXSW) |
| 5 | 5 | [gUO5rQzGOWM](https://www.youtube.com/watch?v=gUO5rQzGOWM) | Daryl Hall - Somebody Like You (Live at SXSW) |
| 6 | 6 | [IrX5MuYT9sI](https://www.youtube.com/watch?v=IrX5MuYT9sI) | Daryl Hall - It&#x27;s Uncanny (Live at SXSW) |

### E07: #7 - Daryl Hall hosts Mutlu &amp; Chuck Prophet on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdm0FCMWSNKYl3blDhH0Yw5

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [mRC5_9xRhlg](https://www.youtube.com/watch?v=mRC5_9xRhlg) | Daryl Hall, Mutlu &amp; Chuck Prophet - Living It (Live From Daryl&#x27;s House) |
| 2 | 2 | [N1zpSaNHK10](https://www.youtube.com/watch?v=N1zpSaNHK10) | Daryl Hall, Mutlu &amp; Chuck Prophet - Foolish Pride (Live From Daryl&#x27;s House) |
| 3 | 3 | [VDnZiIJej8Q](https://www.youtube.com/watch?v=VDnZiIJej8Q) | Daryl Hall, Mutlu &amp; Chuck Prophet - Maneater (Live From Daryl&#x27;s House) |
| 4 | 4 | [noyzrmdZ6YQ](https://www.youtube.com/watch?v=noyzrmdZ6YQ) | Daryl Hall, Mutlu &amp; Chuck Prophet - See What It Brings (Live From Daryl&#x27;s House) |
| 5 | 5 | [hiz9Fo_vrag](https://www.youtube.com/watch?v=hiz9Fo_vrag) | Daryl Hall, Mutlu &amp; Chuck Prophet - Summertime Thing (Live From Daryl&#x27;s House) |
| 6 | 6 | [ChPaZV0uRms](https://www.youtube.com/watch?v=ChPaZV0uRms) | Daryl Hall, Mutlu &amp; Chuck Prophet - Soul Sister (Live From Daryl&#x27;s House) |
| 7 | 7 | [V0n-JPdSfQs](https://www.youtube.com/watch?v=V0n-JPdSfQs) | Daryl Hall, Mutlu &amp; Chuck Prophet - You Did (Live From Daryl&#x27;s House) |
| 8 | 8 | [N1zpSaNHK10](https://www.youtube.com/watch?v=N1zpSaNHK10) | Daryl Hall, Mutlu &amp; Chuck Prophet - Foolish Pride (Live From Daryl&#x27;s House) |
| 9 | 9 | [Vyn4NrMt-II](https://www.youtube.com/watch?v=Vyn4NrMt-II) | Daryl Hall, Mutlu &amp; Chuck Prophet - You Make My Dreams (Live From Daryl&#x27;s House) |

### E08: #8 - Daryl Hall hosts Nick Lowe on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveHWyTBiIcA_d5K1Tdl2f4q

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [PooHY9hhdoU](https://www.youtube.com/watch?v=PooHY9hhdoU) | Daryl Hall &amp; Nick Lowe - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [Chhv-0cnZ34](https://www.youtube.com/watch?v=Chhv-0cnZ34) | Daryl Hall &amp; Nick Lowe - I Live On A Battlefield (Live From Daryl&#x27;s House) |
| 3 | 3 | [6hQoZE2kmdI](https://www.youtube.com/watch?v=6hQoZE2kmdI) | Daryl Hall &amp; Nick Lowe - Time I Took A Holiday (Live From Daryl&#x27;s House) |
| 4 | 4 | [pcUFyhR6KU0](https://www.youtube.com/watch?v=pcUFyhR6KU0) | Daryl Hall &amp; Nick Lowe - Cruel To Be Kind (Live From Daryl&#x27;s House) |
| 5 | 5 | [V0yBf-rZqPA](https://www.youtube.com/watch?v=V0yBf-rZqPA) | Daryl Hall &amp; Nick Lowe - Shelley My Love (Live From Daryl&#x27;s House) |
| 6 | 6 | [VrNQIqoRU_I](https://www.youtube.com/watch?v=VrNQIqoRU_I) | Daryl Hall &amp; Nick Lowe - Rome Wasn&#x27;t Built In A Day (Live From Daryl&#x27;s House) |
| 7 | 7 | [JUWdsIGbLeU](https://www.youtube.com/watch?v=JUWdsIGbLeU) | Daryl Hall &amp; Nick Lowe - Perkiomen (Live From Daryl&#x27;s House) |
| 8 | 8 | [BSUJBOJdZTw](https://www.youtube.com/watch?v=BSUJBOJdZTw) | Daryl Hall &amp; Nick Lowe - End (Live From Daryl&#x27;s House) |

### E09: #9 - Daryl Hall hosts Monte Montgomery on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc_n32YOAgp748VrRJULdPy

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [bdf-GNhF6U0](https://www.youtube.com/watch?v=bdf-GNhF6U0) | Daryl Hall &amp; Monte Montgomery - Loved You Forever (Live From Daryl&#x27;s House) |
| 2 | 2 | [WPLlpOrTQdc](https://www.youtube.com/watch?v=WPLlpOrTQdc) | Daryl Hall &amp; Monte Montgomery - That&#x27;s The Way I Feel About You (Live From Daryl&#x27;s House) |
| 3 | 3 | [RVEuZ49zkbg](https://www.youtube.com/watch?v=RVEuZ49zkbg) | Daryl Hall &amp; Monte Montgomery - Northstar (Live From Daryl&#x27;s House) |
| 4 | 4 | [UmyG0zjSwT4](https://www.youtube.com/watch?v=UmyG0zjSwT4) | Daryl Hall &amp; Monte Montgomery - Sitting On The Dock Of The Bay (Live From Daryl&#x27;s House) |
| 5 | 5 | [EACF8ZvYipM](https://www.youtube.com/watch?v=EACF8ZvYipM) | Daryl Hall &amp; Monte Montgomery - Do It For Love (Live From Daryl&#x27;s House) |
| 6 | 6 | [vFkWbleNtCk](https://www.youtube.com/watch?v=vFkWbleNtCk) | Daryl Hall &amp; Monte Montgomery - Dreamtime (Live From Daryl&#x27;s House) |
| 7 | 7 | [IexJplCNFIk](https://www.youtube.com/watch?v=IexJplCNFIk) | Daryl Hall &amp; Monte Montgomery - Sara Smile (Live From Daryl&#x27;s House) |
| 8 | 8 | [SB0KC4ip01g](https://www.youtube.com/watch?v=SB0KC4ip01g) | Daryl Hall &amp; Monte Montgomery - Midlife Matinee (Live From Daryl&#x27;s House) |

### E10: #10 - Daryl Hall hosts Chromeo on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveEcVjY6caUTMQ3BEJQJ5rC

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [miR9REbP0KE](https://www.youtube.com/watch?v=miR9REbP0KE) | Daryl Hall &amp; Chromeo - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [vI1apCjJFec](https://www.youtube.com/watch?v=vI1apCjJFec) | Daryl Hall &amp; Chromeo - Adult Education (Live From Daryl&#x27;s House) |
| 3 | 3 | [tSiiImDp14g](https://www.youtube.com/watch?v=tSiiImDp14g) | Daryl Hall &amp; Chromeo - Family Man (Live From Daryl&#x27;s House) |
| 4 | 4 | [wHY7w88mYrk](https://www.youtube.com/watch?v=wHY7w88mYrk) | Daryl Hall &amp; Chromeo - Fantasy Is Reality (Live From Daryl&#x27;s House) |
| 5 | 5 | [gt1ueWTrNyU](https://www.youtube.com/watch?v=gt1ueWTrNyU) | Daryl Hall &amp; Chromeo - Lowdown (Live From Daryl&#x27;s House) |
| 6 | 6 | [Qxtkcher-tc](https://www.youtube.com/watch?v=Qxtkcher-tc) | Daryl Hall &amp; Chromeo - Method Of Modern Love (Live From Daryl&#x27;s House) |
| 7 | 7 | [cGRHGz0OcMo](https://www.youtube.com/watch?v=cGRHGz0OcMo) | Daryl Hall &amp; Chromeo - I Can&#x27;t Go For That (No Can Do) (Live From Daryl&#x27;s House) |
| 8 | 8 | [bMc-2QIyY-M](https://www.youtube.com/watch?v=bMc-2QIyY-M) | Daryl Hall &amp; Chromeo - Tenderoni (Live From Daryl&#x27;s House) |
| 9 | 9 | [T2gb5z3fhrE](https://www.youtube.com/watch?v=T2gb5z3fhrE) | Daryl Hall &amp; Chromeo - Waiting For You (Live From Daryl&#x27;s House) |
| 10 | 10 | [kxMS9BXgVX0](https://www.youtube.com/watch?v=kxMS9BXgVX0) | Daryl Hall &amp; Chromeo - End (Live From Daryl&#x27;s House) |

### E11: #11 - Daryl Hall hosts Finger Eleven on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdhH5L9tu_yPt4VRzRZjVsN

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Iz0hWfWGG0M](https://www.youtube.com/watch?v=Iz0hWfWGG0M) | Daryl Hall &amp; Finger Eleven - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [Iz7kcQxUWhI](https://www.youtube.com/watch?v=Iz7kcQxUWhI) | Daryl Hall &amp; Finger Eleven - I&#x27;ll Keep Your Memory Vague (Live From Daryl&#x27;s House) |
| 3 | 3 | [FFlwrzAfqyw](https://www.youtube.com/watch?v=FFlwrzAfqyw) | Daryl Hall &amp; Finger Eleven - Paralyzer (Live From Daryl&#x27;s House) |
| 4 | 4 | [wv-WkaEuaKQ](https://www.youtube.com/watch?v=wv-WkaEuaKQ) | Daryl Hall &amp; Finger Eleven - Falling On (Live From Daryl&#x27;s House) |
| 5 | 5 | [YySMAPrsvSA](https://www.youtube.com/watch?v=YySMAPrsvSA) | Daryl Hall &amp; Finger Eleven - Talking To The Walls (Live From Daryl&#x27;s House) |
| 6 | 6 | [RC4Jl9feR6M](https://www.youtube.com/watch?v=RC4Jl9feR6M) | Daryl Hall &amp; Finger Eleven - Family Man (Live From Daryl&#x27;s House) |
| 7 | 7 | [lbTBjju_f9E](https://www.youtube.com/watch?v=lbTBjju_f9E) | Daryl Hall &amp; Finger Eleven - Art Of Heartbreak (Live From Daryl&#x27;s House) |
| 8 | 8 | [0SPy2EQNBX8](https://www.youtube.com/watch?v=0SPy2EQNBX8) | Daryl Hall &amp; Finger Eleven - Romeo Is Bleeding (Live From Daryl&#x27;s House) |
| 9 | 9 | [Qq08A9UjRTA](https://www.youtube.com/watch?v=Qq08A9UjRTA) | Daryl Hall &amp; Finger Eleven - Ain&#x27;t No Sunshine (Live From Daryl&#x27;s House) |
| 10 | 10 | [VV0Nl6gHX74](https://www.youtube.com/watch?v=VV0Nl6gHX74) | Daryl Hall &amp; Finger Eleven - End (Live From Daryl&#x27;s House) |

### E12: #12 - Daryl Hall hosts Eric Hutchinson on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdu1jLkyBOxVen5sAGSzOo-

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [9vfFiKAvKyI](https://www.youtube.com/watch?v=9vfFiKAvKyI) | Daryl Hall &amp; Eric Hutchinson - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [4PknsIq5myo](https://www.youtube.com/watch?v=4PknsIq5myo) | Daryl Hall &amp; Eric Hutchinson - Tell Me Something Good (Live From Daryl&#x27;s House) |
| 3 | 3 | [cl1R11N_geg](https://www.youtube.com/watch?v=cl1R11N_geg) | Daryl Hall &amp; Eric Hutchinson - I Don&#x27;t Wanna Lose You (Live From Daryl&#x27;s House) |
| 4 | 4 | [fyeMt-2D2bE](https://www.youtube.com/watch?v=fyeMt-2D2bE) | Daryl Hall &amp; Eric Hutchinson - Private Eyes (Live From Daryl&#x27;s House) |
| 5 | 5 | [TOalnR_q0gA](https://www.youtube.com/watch?v=TOalnR_q0gA) | Daryl Hall &amp; Eric Hutchinson - Rock and Roll (Live From Daryl&#x27;s House) |
| 6 | 6 | [Z43q-1BmDg0](https://www.youtube.com/watch?v=Z43q-1BmDg0) | Daryl Hall &amp; Eric Hutchinson - Ok, It&#x27;s Alright With Me (Live From Daryl&#x27;s House) |
| 7 | 7 | [MPLlc9zNXYM](https://www.youtube.com/watch?v=MPLlc9zNXYM) | Daryl Hall &amp; Eric Hutchinson - Food Chain (Live From Daryl&#x27;s House) |
| 8 | 8 | [ZSRjhKtsx1w](https://www.youtube.com/watch?v=ZSRjhKtsx1w) | Daryl Hall &amp; Eric Hutchinson - You Don&#x27;t Have To Believe Me (Live From Daryl&#x27;s House) |
| 9 | 9 | [tLsyUNMpzOU](https://www.youtube.com/watch?v=tLsyUNMpzOU) | Daryl Hall &amp; Eric Hutchinson - Tracks Of My Tears (Live From Daryl&#x27;s House) |
| 10 | 10 | [fZWgHhF3rJs](https://www.youtube.com/watch?v=fZWgHhF3rJs) | Daryl Hall &amp; Eric Hutchinson - End (Live From Daryl&#x27;s House) |

### E14: #14 - Daryl Hall hosts Kevin Rudolf on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdGhsk543B0rZQUOiQ3V31s

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [k3EDIYHpVzU](https://www.youtube.com/watch?v=k3EDIYHpVzU) | Daryl Hall &amp; Kevin Rudolf - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [iKwfRqh0GUk](https://www.youtube.com/watch?v=iKwfRqh0GUk) | Daryl Hall &amp; Kevin Rudolf - Welcome To The World (Live From Daryl&#x27;s House) |
| 3 | 3 | [CyO3Gf4wVjM](https://www.youtube.com/watch?v=CyO3Gf4wVjM) | Daryl Hall &amp; Kevin Rudolf - I Song (Live From Daryl&#x27;s House) |
| 4 | 4 | [vLpu8axxQR4](https://www.youtube.com/watch?v=vLpu8axxQR4) | Daryl Hall &amp; Kevin Rudolf - What&#x27;s Going On (Live From Daryl&#x27;s House) |
| 5 | 5 | [k1NNp9PzJS0](https://www.youtube.com/watch?v=k1NNp9PzJS0) | Daryl Hall &amp; Kevin Rudolf - Beast of Burden (Live From Daryl&#x27;s House) |
| 6 | 6 | [fYnR57FQUPY](https://www.youtube.com/watch?v=fYnR57FQUPY) | Daryl Hall &amp; Kevin Rudolf - In The City (Live From Daryl&#x27;s House) |
| 7 | 7 | [J2ydV0r3yuo](https://www.youtube.com/watch?v=J2ydV0r3yuo) | Daryl Hall &amp; Kevin Rudolf - Let It Rock (Live From Daryl&#x27;s House) |
| 8 | 8 | [Fz0RKybnwzs](https://www.youtube.com/watch?v=Fz0RKybnwzs) | Daryl Hall &amp; Kevin Rudolf - Everyday Will Be Like A Holiday (Live From Daryl&#x27;s House) |
| 9 | 9 | [9d_TXxOsweM](https://www.youtube.com/watch?v=9d_TXxOsweM) | Daryl Hall &amp; Kevin Rudolf - She&#x27;s Gone (Live From Daryl&#x27;s House) |
| 10 | 10 | [GCS_QOV0RxM](https://www.youtube.com/watch?v=GCS_QOV0RxM) | Daryl Hall &amp; Kevin Rudolf - End (Live From Daryl&#x27;s House) |

### E15: #15 - Daryl Hall hosts Company Of Thieves on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdkj1zJsPh_hVKXRyEfxMQM

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Sk2gTnP5dK8](https://www.youtube.com/watch?v=Sk2gTnP5dK8) | Daryl Hall &amp; Company Of Thieves - Pressure (Live From Daryl&#x27;s House) |
| 2 | 2 | [M8DEN1ey4hU](https://www.youtube.com/watch?v=M8DEN1ey4hU) | Daryl Hall &amp; Company Of Thieves - Around The Block (Live From Daryl&#x27;s House) |
| 3 | 3 | [Zz0bzKTPGB8](https://www.youtube.com/watch?v=Zz0bzKTPGB8) | Daryl Hall &amp; Company Of Thieves - Even in The Dark (Live From Daryl&#x27;s House) |
| 4 | 4 | [dxvUdo1PRaM](https://www.youtube.com/watch?v=dxvUdo1PRaM) | Daryl Hall &amp; Company Of Thieves - Past The Sleep (Live From Daryl&#x27;s House) |
| 5 | 5 | [xrizFK8fZ1E](https://www.youtube.com/watch?v=xrizFK8fZ1E) | Daryl Hall &amp; Company Of Thieves - Time of the Season (Live From Daryl&#x27;s House) |
| 6 | 6 | [DAipI7Ox_5c](https://www.youtube.com/watch?v=DAipI7Ox_5c) | Daryl Hall &amp; Company Of Thieves - Piece of My Heart (Live From Daryl&#x27;s House) |
| 7 | 7 | [H-5M6ZJpYss](https://www.youtube.com/watch?v=H-5M6ZJpYss) | Daryl Hall &amp; Company Of Thieves - Starting All Over Again (Live From Daryl&#x27;s House) |
| 8 | 8 | [b52MHf-GiV4](https://www.youtube.com/watch?v=b52MHf-GiV4) | Daryl Hall &amp; Company Of Thieves - Everytime You Go Away (Live From Daryl&#x27;s House) |

### E16: #16 - Daryl Hall hosts The Bacon Brothers on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc28o-RIKn9gy-OQRV--fa9

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [6ADZSgcnBXc](https://www.youtube.com/watch?v=6ADZSgcnBXc) | Daryl Hall &amp; The Bacon Brothers - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [IhNbw-lQqYE](https://www.youtube.com/watch?v=IhNbw-lQqYE) | Daryl Hall &amp; The Bacon Brothers - Above The Clouds (Live From Daryl&#x27;s House) |
| 3 | 3 | [bQI4lqcqbWc](https://www.youtube.com/watch?v=bQI4lqcqbWc) | Daryl Hall &amp; The Bacon Brothers - It&#x27;s All Over Now (Live From Daryl&#x27;s House) |
| 4 | 4 | [hpS-nmGY8Pw](https://www.youtube.com/watch?v=hpS-nmGY8Pw) | Daryl Hall &amp; The Bacon Brothers - Tell Me What I Have To Do (Live From Daryl&#x27;s House) |
| 5 | 5 | [5yRXPX1SoZE](https://www.youtube.com/watch?v=5yRXPX1SoZE) | Daryl Hall &amp; The Bacon Brothers - Bunch Of Words (Live From Daryl&#x27;s House) |
| 6 | 6 | [_nXLhuSOLC0](https://www.youtube.com/watch?v=_nXLhuSOLC0) | Daryl Hall &amp; The Bacon Brothers - Go My Way (The iPod Song) (Live From Daryl&#x27;s House) |
| 7 | 7 | [BPVJLtuGeZc](https://www.youtube.com/watch?v=BPVJLtuGeZc) | Daryl Hall &amp; The Bacon Brothers - New Year&#x27;s Day (Live From Daryl&#x27;s House) |
| 8 | 8 | [Seb_0BIuRYk](https://www.youtube.com/watch?v=Seb_0BIuRYk) | Daryl Hall &amp; The Bacon Brothers - When The Morning Comes (Live From Daryl&#x27;s House) |
| 9 | 9 | [9SI26UpQjeo](https://www.youtube.com/watch?v=9SI26UpQjeo) | Daryl Hall &amp; The Bacon Brothers - The Last Time (Live From Daryl&#x27;s House) |
| 10 | 10 | [qmbN8OCDrDc](https://www.youtube.com/watch?v=qmbN8OCDrDc) | Daryl Hall &amp; The Bacon Brothers - End (Live From Daryl&#x27;s House) |

### E17: #17 - Daryl Hall hosts Matt Nathanson on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcU64m47bOrrou818Vg87ZW

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [OG-tyfLuFE0](https://www.youtube.com/watch?v=OG-tyfLuFE0) | Daryl Hall &amp; Matt Nathanson - Come On Get Higher (Live From Daryl&#x27;s House) |
| 2 | 2 | [HFGJ583HYhE](https://www.youtube.com/watch?v=HFGJ583HYhE) | Daryl Hall &amp; Matt Nathanson - Car Crash (Live From Daryl&#x27;s House) |
| 3 | 3 | [F0gg42Ynd1Q](https://www.youtube.com/watch?v=F0gg42Ynd1Q) | Daryl Hall &amp; Matt Nathanson - Still (Live From Daryl&#x27;s House) |
| 4 | 4 | [svO005FYr9A](https://www.youtube.com/watch?v=svO005FYr9A) | Daryl Hall &amp; Matt Nathanson - Did It In A Minute (Live From Daryl&#x27;s House) |
| 5 | 5 | [M3npu_UwhLA](https://www.youtube.com/watch?v=M3npu_UwhLA) | Daryl Hall &amp; Matt Nathanson - Wishing Well (Live From Daryl&#x27;s House) |
| 6 | 6 | [WfJxqYC5AuU](https://www.youtube.com/watch?v=WfJxqYC5AuU) | Daryl Hall &amp; Matt Nathanson - The Weight (Live From Daryl&#x27;s House) |
| 7 | 7 | [PO4AA5806x4](https://www.youtube.com/watch?v=PO4AA5806x4) | Daryl Hall &amp; Matt Nathanson - All We Are (Live From Daryl&#x27;s House) |
| 8 | 8 | [iXyEg87KmtU](https://www.youtube.com/watch?v=iXyEg87KmtU) | Daryl Hall &amp; Matt Nathanson - One On One (Live From Daryl&#x27;s House) |

### E18: #18 - Daryl Hall hosts Robby Krieger and Ray Manzarek of The Doors on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc52PZ0NFqoM2IGlUwXvX18

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [GxeVn38BpEI](https://www.youtube.com/watch?v=GxeVn38BpEI) | Daryl Hall &amp; The Doors - People Are Strange (Live From Daryl&#x27;s House) |
| 2 | 2 | [cz_Ohc0W3t4](https://www.youtube.com/watch?v=cz_Ohc0W3t4) | Daryl Hall &amp; The Doors - Family Affair (Live From Daryl&#x27;s House) |
| 3 | 3 | [iIVvaF8pWZA](https://www.youtube.com/watch?v=iIVvaF8pWZA) | Daryl Hall &amp; The Doors - The Crystal Ship (Live From Daryl&#x27;s House) |
| 4 | 4 | [v4oq890avac](https://www.youtube.com/watch?v=v4oq890avac) | Daryl Hall &amp; The Doors - Roadhouse Blues (Live From Daryl&#x27;s House) |
| 5 | 5 | [Z_GdFo4tuDs](https://www.youtube.com/watch?v=Z_GdFo4tuDs) | Daryl Hall &amp; The Doors - Break On Through (Live From Daryl&#x27;s House) |
| 6 | 6 | [z3-hg3mtpfc](https://www.youtube.com/watch?v=z3-hg3mtpfc) | Daryl Hall &amp; The Doors - Borderline (Live From Daryl&#x27;s House) |
| 7 | 7 | [IN2tnRS_j-0](https://www.youtube.com/watch?v=IN2tnRS_j-0) | Daryl Hall &amp; The Doors - Kiss On My List (Live From Daryl&#x27;s House) |

### E19: #19 - Retrospective

https://www.youtube.com/playlist?list=PLINSQGXREtvfbCL6Mly4EKIAPdHWKh5aX

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [rFF6ciRfdRs](https://www.youtube.com/watch?v=rFF6ciRfdRs) | Daryl Hall - Our Day Will Come |
| 2 | 2 | [3xpGUG3RNSw](https://www.youtube.com/watch?v=3xpGUG3RNSw) | Daryl Hall - In My Own Dream |
| 3 | 3 | [YkEwqawDbYw](https://www.youtube.com/watch?v=YkEwqawDbYw) | Daryl Hall - You&#x27;re A Big Girl Now |
| 4 | 4 | [ybVmlFYqj8E](https://www.youtube.com/watch?v=ybVmlFYqj8E) | Daryl Hall - White Port Lemon Juice |
| 5 | 5 | [a4tGHrBiqSM](https://www.youtube.com/watch?v=a4tGHrBiqSM) | Daryl Hall - Neither One Of Us (Live From Daryl&#x27;s House) |
| 6 | 6 | [T9R-JIhhLwM](https://www.youtube.com/watch?v=T9R-JIhhLwM) | Daryl Hall Retrospective 1 - End |

### E20: #20 - Daryl Hall hosts Parachute on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveSxwUP0sJlr41uTr_XDmKM

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [MOWaoU18h9k](https://www.youtube.com/watch?v=MOWaoU18h9k) | Daryl Hall &amp; Parachute - Under Control (Live From Daryl&#x27;s House) |
| 2 | 2 | [Rq-4VLCpbOk](https://www.youtube.com/watch?v=Rq-4VLCpbOk) | Daryl Hall &amp; Parachute - She Is Love (Live From Daryl&#x27;s House) |
| 3 | 3 | [2gLO7LPciRc](https://www.youtube.com/watch?v=2gLO7LPciRc) | Daryl Hall &amp; Parachute - All That I Am (Live From Daryl&#x27;s House) |
| 4 | 4 | [q31DMAfiBrQ](https://www.youtube.com/watch?v=q31DMAfiBrQ) | Daryl Hall &amp; Parachute - She (for Liz) (Live From Daryl&#x27;s House) |
| 5 | 5 | [UqjWqxBnfag](https://www.youtube.com/watch?v=UqjWqxBnfag) | Daryl Hall &amp; Parachute - It&#x27;s A Laugh (Live From Daryl&#x27;s House) |
| 6 | 6 | [5OaJeUtZiiQ](https://www.youtube.com/watch?v=5OaJeUtZiiQ) | Daryl Hall &amp; Parachute - Shotgun (Live From Daryl&#x27;s House) |
| 7 | 7 | [05CcGa8EL6g](https://www.youtube.com/watch?v=05CcGa8EL6g) | Daryl Hall &amp; Parachute - Say It Isn&#x27;t So (Live From Daryl&#x27;s House) |

### E21: #21 - Daryl Hall hosts Plain White T&#x27;s on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcV2uzbeuPJL-4lj_elLw2M

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [GbWfjpAPrKs](https://www.youtube.com/watch?v=GbWfjpAPrKs) | Daryl Hall &amp; Plain White T&#x27;s - Sunlight (Live From Daryl&#x27;s House) |
| 2 | 2 | [JLGyajn0qm0](https://www.youtube.com/watch?v=JLGyajn0qm0) | Daryl Hall &amp; Plain White T&#x27;s - Starting All Over Again (Live From Daryl&#x27;s House) |
| 3 | 3 | [4GZf0nlChfQ](https://www.youtube.com/watch?v=4GZf0nlChfQ) | Daryl Hall &amp; Plain White T&#x27;s - Is She Really Going Out With Him (Live From Daryl&#x27;s House) |
| 4 | 4 | [li9b1reuCtk](https://www.youtube.com/watch?v=li9b1reuCtk) | Daryl Hall &amp; Plain White T&#x27;s - Rainy Day (Live From Daryl&#x27;s House) |
| 5 | 5 | [opFFyKu6tm8](https://www.youtube.com/watch?v=opFFyKu6tm8) | Daryl Hall &amp; Plain White Ts - So Close (Live From Daryl&#x27;s House) |
| 6 | 6 | [tYJaBWeVPkE](https://www.youtube.com/watch?v=tYJaBWeVPkE) | Daryl Hall &amp; Plain White T&#x27;s - Hey There Delilah (Live From Daryl&#x27;s House) |
| 7 | 7 | [XXus-pvvY5o](https://www.youtube.com/watch?v=XXus-pvvY5o) | Daryl Hall &amp; Plain White T&#x27;s - 1, 2, 3, 4 (Live From Daryl&#x27;s House) |
| 8 | 8 | [UoV0Rw-9kKc](https://www.youtube.com/watch?v=UoV0Rw-9kKc) | Daryl Hall &amp; Plain White T&#x27;s - End (Live From Daryl&#x27;s House) |

### E22: #22 - Daryl Hall hosts Smokey Robinson on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcZBYfgAB-yMv_7DtIaULIp

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [zKNpWpkA6f4](https://www.youtube.com/watch?v=zKNpWpkA6f4) | Daryl Hall &amp; Smokey Robinson - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [bULuGNEMpi8](https://www.youtube.com/watch?v=bULuGNEMpi8) | Daryl Hall &amp; Smokey Robinson - Being With You (Live From Daryl&#x27;s House) |
| 3 | 3 | [JYM0m7XmHv4](https://www.youtube.com/watch?v=JYM0m7XmHv4) | Daryl Hall &amp; Smokey Robinson - Girlfriend (Live From Daryl&#x27;s House) |
| 4 | 4 | [NlzWBrOArYA](https://www.youtube.com/watch?v=NlzWBrOArYA) | Daryl Hall &amp; Smokey Robinson - Don&#x27;t Know Why (Live From Daryl&#x27;s House) |
| 5 | 5 | [s2tE4lJLnFo](https://www.youtube.com/watch?v=s2tE4lJLnFo) | Daryl Hall &amp; Smokey Robinson - Tears Of A Clown (Live From Daryl&#x27;s House) |
| 6 | 6 | [goUz1L9LRCA](https://www.youtube.com/watch?v=goUz1L9LRCA) | Daryl Hall &amp; Smokey Robinson - Going To A Go Go (Live From Daryl&#x27;s House) |
| 7 | 7 | [tsJ_J5KVKLM](https://www.youtube.com/watch?v=tsJ_J5KVKLM) | Daryl Hall &amp; Smokey Robinson - Sara Smile / Ooh Baby Baby (Live From Daryl&#x27;s House) |
| 8 | 8 | [EAh5DseKbl4](https://www.youtube.com/watch?v=EAh5DseKbl4) | Daryl Hall &amp; Smokey Robinson - I Can&#x27;t Go For That (No Can Do) (Live From Daryl&#x27;s House) |
| 9 | 9 | [Tc1vj3KN4eA](https://www.youtube.com/watch?v=Tc1vj3KN4eA) | Daryl Hall &amp; Smokey Robinson - I&#x27;ve Been Good To You (Live From Daryl&#x27;s House) |

### E23: #23 - Daryl Hall hosts Todd Rundgren on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtve4nqpvEEXKmBk1iAik0Iiq

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [eKzRHX0hHt8](https://www.youtube.com/watch?v=eKzRHX0hHt8) | Daryl Hall &amp; Todd Rundgren - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [4Vi4gTa1P9U](https://www.youtube.com/watch?v=4Vi4gTa1P9U) | Daryl Hall &amp; Todd Rundgren - Expressway To Your Heart (Live From Daryl&#x27;s House) |
| 3 | 3 | [naY4pCFChJY](https://www.youtube.com/watch?v=naY4pCFChJY) | Daryl Hall &amp; Todd Rundgren - Sweet (Live From Daryl&#x27;s House) |
| 4 | 4 | [rmRrqBFFVog](https://www.youtube.com/watch?v=rmRrqBFFVog) | Daryl Hall &amp; Todd Rundgren - The Want Of A Nail (Live From Daryl&#x27;s House) |
| 5 | 5 | [UQJEJPqnW9I](https://www.youtube.com/watch?v=UQJEJPqnW9I) | Daryl Hall &amp; Todd Rundgren - Sometimes I Don&#x27;t Know How To Feel (Live From Daryl&#x27;s House) |
| 6 | 6 | [a43Io_NtLr4](https://www.youtube.com/watch?v=a43Io_NtLr4) | Daryl Hall &amp; Todd Rundgren - Can We Still Be Friends (Live From Daryl&#x27;s House) |
| 7 | 7 | [zz219n2-9I8](https://www.youtube.com/watch?v=zz219n2-9I8) | Daryl Hall &amp; Todd Rundgren - You Got It (Live From Daryl&#x27;s House) |
| 8 | 8 | [x_QZHhF5BDU](https://www.youtube.com/watch?v=x_QZHhF5BDU) | Daryl Hall &amp; Todd Rundgren - Watch Your Back (Live From Daryl&#x27;s House) |
| 9 | 9 | [w1EBRqDauCY](https://www.youtube.com/watch?v=w1EBRqDauCY) | Daryl Hall &amp; Todd Rundgren - Wait For Me (Live From Daryl&#x27;s House)(Live From Daryl&#x27;s House) |
| 10 | 10 | [gdR7jF7x1JI](https://www.youtube.com/watch?v=gdR7jF7x1JI) | Daryl Hall &amp; Todd Rundgren - End (Live From Daryl&#x27;s House) |

### E24: #24 - Daryl Hall hosts Diane Birch on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveKou9G_zF_acHO6KhSF1nt

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Rw3cJO8rkrQ](https://www.youtube.com/watch?v=Rw3cJO8rkrQ) | Daryl Hall &amp; Diane Birch - Don&#x27;t Wait Up (Live From Daryl&#x27;s House) |
| 2 | 2 | [NKSuaHq-toA](https://www.youtube.com/watch?v=NKSuaHq-toA) | Daryl Hall &amp; Diane Birch - Nothing But A Miracle (Live From Daryl&#x27;s House) |
| 3 | 3 | [Q5oQqDS_d88](https://www.youtube.com/watch?v=Q5oQqDS_d88) | Daryl Hall &amp; Diane Birch - Fire Escape (Live From Daryl&#x27;s House) |
| 4 | 4 | [8Mkkt6t4ssc](https://www.youtube.com/watch?v=8Mkkt6t4ssc) | Daryl Hall &amp; Diane Birch - Life&#x27;s Too Short (Live From Daryl&#x27;s House) |
| 5 | 5 | [TLDYvAq3ZWk](https://www.youtube.com/watch?v=TLDYvAq3ZWk) | Daryl Hall &amp; Diane Birch - Fools (Live From Daryl&#x27;s House) |
| 6 | 6 | [Di9ntbrRUZA](https://www.youtube.com/watch?v=Di9ntbrRUZA) | Daryl Hall &amp; Diane Birch - Fall In Philadelphia (Live From Daryl&#x27;s House) |
| 7 | 7 | [FPYJUxTOy7s](https://www.youtube.com/watch?v=FPYJUxTOy7s) | Daryl Hall &amp; Diane Birch - Daydreaming (Live From Daryl&#x27;s House) |
| 8 | 8 | [PxJnypWj26w](https://www.youtube.com/watch?v=PxJnypWj26w) | Daryl Hall &amp; Diane Birch - End (Live From Daryl&#x27;s House) |

### E25: #25 - Daryl Hall hosts Patrick Stump of Fall Out Boy on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfJQa7dQsB7CDg8Q8Jig7Xp

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [6nFydXQ6dgw](https://www.youtube.com/watch?v=6nFydXQ6dgw) | Daryl Hall &amp; Patrick Stump - Sugar, We&#x27;re Going Down (Live From Daryl&#x27;s House) |
| 2 | 2 | [xUZHM26t8oo](https://www.youtube.com/watch?v=xUZHM26t8oo) | Daryl Hall &amp; Patrick Stump - I Don&#x27;t Care (Live From Daryl&#x27;s House) |
| 3 | 3 | [gF7OCNGS2xQ](https://www.youtube.com/watch?v=gF7OCNGS2xQ) | Daryl Hall &amp; Patrick Stump - What A Catch, Donnie (Live From Daryl&#x27;s House) |
| 4 | 4 | [ADsQXSQqYb8](https://www.youtube.com/watch?v=ADsQXSQqYb8) | Daryl Hall &amp; Patrick Stump - Sophomore Slump or Comeback of the Year (Live From Daryl&#x27;s House) |
| 5 | 5 | [x0JwmQrl5sk](https://www.youtube.com/watch?v=x0JwmQrl5sk) | Daryl Hall &amp; Patrick Stump - Guessing Games (Live From Daryl&#x27;s House) |
| 6 | 6 | [nwexNH7l-jU](https://www.youtube.com/watch?v=nwexNH7l-jU) | Daryl Hall &amp; Patrick Stump - Out of Touch (Live From Daryl&#x27;s House) |
| 7 | 7 | [wSE1XQNRuiI](https://www.youtube.com/watch?v=wSE1XQNRuiI) | Daryl Hall &amp; Patrick Stump - What Becomes Of The Brokenhearted (Live From Daryl&#x27;s House) |
| 8 | 8 | [tWKyVkReE0k](https://www.youtube.com/watch?v=tWKyVkReE0k) | Daryl Hall &amp; Patrick Stump - End (Live From Daryl&#x27;s House) |

### E26: #26 - Daryl Hall hosts Jimmy Wayne on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveF-xh0wO8eIBknD0e2eZoO

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [8OwHUvTK4f4](https://www.youtube.com/watch?v=8OwHUvTK4f4) | Daryl Hall &amp; Jimmy Wayne - I Didn&#x27;t Come Here To Lose (Live From Daryl&#x27;s House) |
| 2 | 2 | [uadYC1H0RoY](https://www.youtube.com/watch?v=uadYC1H0RoY) | Daryl Hall &amp; Jimmy Wayne - Kerosene Kid (Live From Daryl&#x27;s House) |
| 3 | 3 | [KdRsAELYaiw](https://www.youtube.com/watch?v=KdRsAELYaiw) | Daryl Hall &amp; Jimmy Wayne - Do You Believe Me Now (Live From Daryl&#x27;s House) |
| 4 | 4 | [e0Ji8iJNThM](https://www.youtube.com/watch?v=e0Ji8iJNThM) | Daryl Hall &amp; Jimmy Wayne - I&#x27;ll Never Leave You (Live From Daryl&#x27;s House) |
| 5 | 5 | [J7MRduPW928](https://www.youtube.com/watch?v=J7MRduPW928) | Daryl Hall &amp; Jimmy Wayne - Sara Smile |
| 6 | 6 | [ek5np75DVrY](https://www.youtube.com/watch?v=ek5np75DVrY) | Daryl Hall &amp; Jimmy Wayne - Someone Like You (Live From Daryl&#x27;s House) |
| 7 | 7 | [XCe28cXjmWQ](https://www.youtube.com/watch?v=XCe28cXjmWQ) | Daryl Hall &amp; Jimmy Wayne - Knock On Wood (Live From Daryl&#x27;s House) |

### E27: #27 - Daryl Hall hosts Eli &quot;Paperboy&quot; Reed on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdj1ypoRkQgXKDOL7sbK7uJ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [x1NFwRxwmCE](https://www.youtube.com/watch?v=x1NFwRxwmCE) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Pick Up The Pieces (Live From Daryl&#x27;s House) |
| 2 | 2 | [SCzQq0RjcXc](https://www.youtube.com/watch?v=SCzQq0RjcXc) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - I Need Your Lovin&#x27; (Live From Daryl&#x27;s House) |
| 3 | 3 | [B9U2crPBZso](https://www.youtube.com/watch?v=B9U2crPBZso) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - I Found You Out (Live From Daryl&#x27;s House) |
| 4 | 4 | [Vl6gZwnM4hw](https://www.youtube.com/watch?v=Vl6gZwnM4hw) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Pick A Number (Live From Daryl&#x27;s House) |
| 5 | 5 | [b1XxSStTXfw](https://www.youtube.com/watch?v=b1XxSStTXfw) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Take My Love With You (Live From Daryl&#x27;s House) |
| 6 | 6 | [KLsEdIOHdM8](https://www.youtube.com/watch?v=KLsEdIOHdM8) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Storm Warning (Live From Daryl&#x27;s House) |
| 7 | 7 | [7hlLxQi8fqU](https://www.youtube.com/watch?v=7hlLxQi8fqU) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - It&#x27;s Uncanny (Live From Daryl&#x27;s House) |
| 8 | 8 | [IaYy1WJqZw0](https://www.youtube.com/watch?v=IaYy1WJqZw0) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Starting All Over Again (Live From Daryl&#x27;s House) |
| 9 | 9 | [AaLpW8ulSHQ](https://www.youtube.com/watch?v=AaLpW8ulSHQ) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - I Found A Love (Live From Daryl&#x27;s House) |
| 10 | 10 | [C4XWyZ3O84c](https://www.youtube.com/watch?v=C4XWyZ3O84c) | Daryl Hall &amp; Eli Paperboy Reed - You Can Run On (Live From Daryl&#x27;s House) |

### E28: #28 - Daryl Hall hosts Toots &amp; The Maytals on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfsNIhj9QGMcSyRvbGO_NQc

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [hONcYL6Excg](https://www.youtube.com/watch?v=hONcYL6Excg) | Daryl Hall &amp; Toots and The Maytals - Time Tough (Live From Daryl&#x27;s House) |
| 2 | 2 | [p6g3ODWr6gg](https://www.youtube.com/watch?v=p6g3ODWr6gg) | Daryl Hall &amp; Toots and The Maytals - Funky Kingston (Live From Daryl&#x27;s House) |
| 3 | 3 | [UGt9Jg8Hrok](https://www.youtube.com/watch?v=UGt9Jg8Hrok) | Daryl Hall &amp; Toots and The Maytals - Sweet and Dandy (Live From Daryl&#x27;s House) |
| 4 | 4 | [GdKyVQHCtXk](https://www.youtube.com/watch?v=GdKyVQHCtXk) | Daryl Hall &amp; Toots and the Maytals - Reggae Got Soul (Live From Daryl&#x27;s House) |
| 5 | 5 | [LrahtV9e0W4](https://www.youtube.com/watch?v=LrahtV9e0W4) | Daryl Hall &amp; Toots and the Maytals - 54-46 That&#x27;s My Number (Live From Daryl&#x27;s House) |
| 6 | 6 | [6TRaXyfrkxI](https://www.youtube.com/watch?v=6TRaXyfrkxI) | Daryl Hall &amp; Toots and the Maytals - Monkey Man (Live From Daryl&#x27;s House) |
| 7 | 7 | [Lr-TrlzUvF8](https://www.youtube.com/watch?v=Lr-TrlzUvF8) | Daryl Hall &amp; Toots and the Maytals - You Make My Dreams (Live From Daryl&#x27;s House) |
| 8 | 8 | [vEocv-IxqBk](https://www.youtube.com/watch?v=vEocv-IxqBk) | Daryl Hall &amp; Toots and the Maytals - End (Live From Daryl&#x27;s House) |

### E30: #30 - Daryl Hall&#x27;s Tribute to T-Bone

https://www.youtube.com/playlist?list=PLINSQGXREtvflWAdBuyAKxYLXsA8OZYZu

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [mNA_ktTwAPM](https://www.youtube.com/watch?v=mNA_ktTwAPM) | Tribute to T-Bone - If I Don&#x27;t Have You Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [xd82w6qk9Dw](https://www.youtube.com/watch?v=xd82w6qk9Dw) | Tribute to T-Bone - If I Don&#x27;t Have You (Live From Daryl&#x27;s House) |
| 3 | 3 | [9wDSM7fpGIs](https://www.youtube.com/watch?v=9wDSM7fpGIs) | Tribute to T-Bone - Please Send Me Someone (Intro) (Live From Daryl&#x27;s House) |
| 4 | 4 | [xcOETQuwJIE](https://www.youtube.com/watch?v=xcOETQuwJIE) | Tribute to T-Bone - Please Send Me Someone (Live From Daryl&#x27;s House) |
| 5 | 5 | [csogV5fRq_o](https://www.youtube.com/watch?v=csogV5fRq_o) | Tribute to T-Bone - In The Night (Intro) (Live From Daryl&#x27;s House) |
| 6 | 6 | [Ofd5gChIGP0](https://www.youtube.com/watch?v=Ofd5gChIGP0) | Tribute to T-Bone - In The Night (Live From Daryl&#x27;s House) |
| 7 | 7 | [X2iVTOginLY](https://www.youtube.com/watch?v=X2iVTOginLY) | Tribute to T-Bone - I Miss You (Intro) (Live From Daryl&#x27;s House) |
| 8 | 8 | [mvBpknUcO3U](https://www.youtube.com/watch?v=mvBpknUcO3U) | Tribute to T-Bone - I Miss You (Live From Daryl&#x27;s House) |
| 9 | 9 | [IIFDzepjclY](https://www.youtube.com/watch?v=IIFDzepjclY) | Tribute to T-Bone - Change Of Season (Intro) (Live From Daryl&#x27;s House) |
| 10 | 10 | [MvPYq08awWY](https://www.youtube.com/watch?v=MvPYq08awWY) | Tribute to T-Bone - Change Of Season (Live From Daryl&#x27;s House) |
| 11 | 11 | [DYSlgOoVLNo](https://www.youtube.com/watch?v=DYSlgOoVLNo) | Tribute to T-Bone - Caravan Of Love (Intro) (Live From Daryl&#x27;s House) |
| 12 | 12 | [6zWN5E4esjM](https://www.youtube.com/watch?v=6zWN5E4esjM) | Tribute to T-Bone - Caravan Of Love (Live From Daryl&#x27;s House) |
| 13 | 13 | [PMnI_zF8xlE](https://www.youtube.com/watch?v=PMnI_zF8xlE) | Tribute to T-Bone - The Weight (Intro) (Live From Daryl&#x27;s House) |
| 14 | 14 | [eeSbUKU5aYU](https://www.youtube.com/watch?v=eeSbUKU5aYU) | Tribute to T-Bone Wolk - The Weight (Live From Daryl&#x27;s House) |
| 15 | 15 | [6ruJ0w5yOps](https://www.youtube.com/watch?v=6ruJ0w5yOps) | Tribute to T-Bone - End (Live From Daryl&#x27;s House) |

### E31: #31 - Daryl Hall hosts Rob Thomas of Matchbox 20 on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdzf55J_NPZDRn1rtMLhHbI

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [_kSbFGeHEYs](https://www.youtube.com/watch?v=_kSbFGeHEYs) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [TUOLM6yiDfk](https://www.youtube.com/watch?v=TUOLM6yiDfk) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Disease (Live From Daryl&#x27;s House) |
| 3 | 3 | [Pqorjf-851k](https://www.youtube.com/watch?v=Pqorjf-851k) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Kiss On My List (Live From Daryl&#x27;s House) |
| 4 | 4 | [NqkTJL4vQD0](https://www.youtube.com/watch?v=NqkTJL4vQD0) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Someday (Live From Daryl&#x27;s House) |
| 5 | 5 | [J2CmsGBOxvY](https://www.youtube.com/watch?v=J2CmsGBOxvY) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Heard It Through The Grapevine (Live From Daryl&#x27;s House) |
| 6 | 6 | [dYUZqsjeZVs](https://www.youtube.com/watch?v=dYUZqsjeZVs) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - She&#x27;s Gone (Live From Daryl&#x27;s House) |
| 7 | 7 | [FpEBMq7tsz4](https://www.youtube.com/watch?v=FpEBMq7tsz4) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - 3AM (Live From Daryl&#x27;s House) |
| 8 | 8 | [KmIFZlQQ9vY](https://www.youtube.com/watch?v=KmIFZlQQ9vY) | Daryl Hall &amp; Rob Thomas (Matchbox Twenty) - Ever The Same (Live From Daryl&#x27;s House) |

### E32: #32 - Daryl Hall&#x27;s Retrospective 2 on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveA99ijYCJc744xX7GHJi_m

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [nemjyEg5ORk](https://www.youtube.com/watch?v=nemjyEg5ORk) | Daryl Hall &amp; Smokey Robinson - Sara Smile / Ohh Baby Baby (Intro) |
| 2 | 2 | [tsJ_J5KVKLM](https://www.youtube.com/watch?v=tsJ_J5KVKLM) | Daryl Hall &amp; Smokey Robinson - Sara Smile / Ooh Baby Baby (Live From Daryl&#x27;s House) |
| 3 | 3 | [rmRrqBFFVog](https://www.youtube.com/watch?v=rmRrqBFFVog) | Daryl Hall &amp; Todd Rundgren - The Want Of A Nail (Live From Daryl&#x27;s House) |
| 4 | 4 | [V4VHVJx8zn8](https://www.youtube.com/watch?v=V4VHVJx8zn8) | Daryl Hall &amp; Diane Birch - Daydreaming (Intro) |
| 5 | 5 | [FPYJUxTOy7s](https://www.youtube.com/watch?v=FPYJUxTOy7s) | Daryl Hall &amp; Diane Birch - Daydreaming (Live From Daryl&#x27;s House) |
| 6 | 6 | [qiJ0RiaEwTA](https://www.youtube.com/watch?v=qiJ0RiaEwTA) | Daryl Hall &amp; Eli &quot;Paperboy&#x27; Reed - Pick A Number (Intro) |
| 7 | 7 | [8Rry_PXRPPY](https://www.youtube.com/watch?v=8Rry_PXRPPY) | Daryl Hall &amp; Eli &quot;Paperboy&quot; Reed - Pick A Number (Live From Daryl&#x27;s House) |
| 8 | 8 | [Qov__NTMjGg](https://www.youtube.com/watch?v=Qov__NTMjGg) | Daryl Hall &amp; Toots &amp; The Maytals - Reggae Got Soul (Intro) |
| 9 | 9 | [GdKyVQHCtXk](https://www.youtube.com/watch?v=GdKyVQHCtXk) | Daryl Hall &amp; Toots and the Maytals - Reggae Got Soul (Live From Daryl&#x27;s House) |
| 10 | 10 | [jeNUmTKYNR8](https://www.youtube.com/watch?v=jeNUmTKYNR8) | Tribute to T-Bone - I Miss You (Intro) |
| 11 | 11 | [mvBpknUcO3U](https://www.youtube.com/watch?v=mvBpknUcO3U) | Tribute to T-Bone - I Miss You (Live From Daryl&#x27;s House) |
| 12 | 12 | [6-F00NFAKUY](https://www.youtube.com/watch?v=6-F00NFAKUY) | Daryl Hall &amp; Jimmy Wayne - Kerosene Kid (Intro) |
| 13 | 13 | [uadYC1H0RoY](https://www.youtube.com/watch?v=uadYC1H0RoY) | Daryl Hall &amp; Jimmy Wayne - Kerosene Kid (Live From Daryl&#x27;s House) |
| 14 | 14 | [MRbWIk7DxzM](https://www.youtube.com/watch?v=MRbWIk7DxzM) | Daryl Hall Retrospective 2 - End |

### E33: #33 - Daryl Hall hosts Pat Monahan of Train on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvf9i892uSlIfyHQFdAVnw3K

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Qi1_VOZ-nEQ](https://www.youtube.com/watch?v=Qi1_VOZ-nEQ) | Daryl Hall &amp; Train - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [g7bC2LnVA84](https://www.youtube.com/watch?v=g7bC2LnVA84) | Daryl Hall &amp; Train - I&#x27;m Not Waiting In Line (Live From Daryl&#x27;s House) |
| 3 | 3 | [mfRL9Y133EA](https://www.youtube.com/watch?v=mfRL9Y133EA) | Daryl Hall &amp; Train - Hey, Soul Sister (Live From Daryl&#x27;s House) |
| 4 | 4 | [n4lzW9iW9YQ](https://www.youtube.com/watch?v=n4lzW9iW9YQ) | Daryl Hall &amp; Train - Cab (Live From Daryl&#x27;s House) |
| 5 | 5 | [siGzfAKuR1o](https://www.youtube.com/watch?v=siGzfAKuR1o) | Daryl Hall &amp; Train - If It&#x27;s Love (Live From Daryl&#x27;s House) |
| 6 | 6 | [r6NA_249V3Q](https://www.youtube.com/watch?v=r6NA_249V3Q) | Daryl Hall &amp; Train - Say It Isn&#x27;t So (Live From Daryl&#x27;s House) |
| 7 | 7 | [bnU1vb0UPJY](https://www.youtube.com/watch?v=bnU1vb0UPJY) | Daryl Hall &amp; Train - Wait For Me (Live From Daryl&#x27;s House) |
| 8 | 8 | [G4npc2i7H_0](https://www.youtube.com/watch?v=G4npc2i7H_0) | Daryl Hall &amp; Train - Papa Was A Rolling Stone (Live From Daryl&#x27;s House) |

### E34: #34 - Daryl Hall hosts Sharon Jones on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvciVmXkb3zq5hyCnswL9mwJ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [yf82CIke7Pk](https://www.youtube.com/watch?v=yf82CIke7Pk) | Daryl Hall &amp; Sharon Jones - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [QQlC2UMUgjQ](https://www.youtube.com/watch?v=QQlC2UMUgjQ) | Daryl Hall &amp; Sharon Jones - 100 Days, 100 Nights (Live From Daryl&#x27;s House) |
| 3 | 3 | [VuSNVDeCbeg](https://www.youtube.com/watch?v=VuSNVDeCbeg) | Daryl Hall &amp; Sharon Jones - Tell Me (Live From Daryl&#x27;s House) |
| 4 | 4 | [qjrQpVceMws](https://www.youtube.com/watch?v=qjrQpVceMws) | Daryl Hall &amp; Sharon Jones - Uncanny (Live From Daryl&#x27;s House) |
| 5 | 5 | [iEWDVZY3kWQ](https://www.youtube.com/watch?v=iEWDVZY3kWQ) | Daryl Hall &amp; Sharon Jones - I Learned The Hard Way (Live From Daryl&#x27;s House) |
| 6 | 6 | [X-OtjioTB-Y](https://www.youtube.com/watch?v=X-OtjioTB-Y) | Daryl Hall &amp; Sharon Jones - Do What You Want, Be What You Are (Live From Daryl&#x27;s House) |
| 7 | 7 | [aymW_IHqJrg](https://www.youtube.com/watch?v=aymW_IHqJrg) | Daryl Hall &amp; Sharon Jones - Got A Thing On My Mind (Live From Daryl&#x27;s House) |
| 8 | 8 | [J81HcXsCW-Q](https://www.youtube.com/watch?v=J81HcXsCW-Q) | Daryl Hall &amp; Sharon Jones - Hot Fun In The Summertime (Live From Daryl&#x27;s House) |
| 9 | 9 | [izKopKZa4nE](https://www.youtube.com/watch?v=izKopKZa4nE) | Daryl Hall &amp; Sharon Jones - End (Live From Daryl&#x27;s House) |

### E35: #35 - Daryl Hall hosts Fitz and The Tantrums on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtve85S8RDwWJy0IJtaqmcHa7

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [6OnRsCDRQFI](https://www.youtube.com/watch?v=6OnRsCDRQFI) | Daryl Hall &amp; Fitz and the Tantrums - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [YIN3zmQFgVI](https://www.youtube.com/watch?v=YIN3zmQFgVI) | Daryl Hall &amp; Fitz and the Tantrums - Pickin&#x27; Up The Pieces (Live From Daryl&#x27;s House) |
| 3 | 3 | [ajWrCO5LgWo](https://www.youtube.com/watch?v=ajWrCO5LgWo) | Daryl Hall &amp; Fitz and the Tantrums - Breakin&#x27; The Chains Of Love (Live From Daryl&#x27;s House) |
| 4 | 4 | [IRDr3L-Javo](https://www.youtube.com/watch?v=IRDr3L-Javo) | Daryl Hall &amp; Fitz and the Tantrums - Dear Mr. President (Live From Daryl&#x27;s House) |
| 5 | 5 | [r358XTi8UZo](https://www.youtube.com/watch?v=r358XTi8UZo) | Daryl Hall &amp; Fitz and the Tantrums - Perkiomen (Live From Daryl&#x27;s House) |
| 6 | 6 | [cpJWVbboGXk](https://www.youtube.com/watch?v=cpJWVbboGXk) | Daryl Hall &amp; Fitz and the Tantrums - Girl, I Love You (Live From Daryl&#x27;s House) |
| 7 | 7 | [JySlsoOTVUQ](https://www.youtube.com/watch?v=JySlsoOTVUQ) | Daryl Hall &amp; Fitz and the Tantrums - MoneyGrabber (Live From Daryl&#x27;s House) |
| 8 | 8 | [uYByVf_TS_Q](https://www.youtube.com/watch?v=uYByVf_TS_Q) | Daryl Hall &amp; Fitz and the Tantrums - Sara Smile (Live From Daryl&#x27;s House) |
| 9 | 9 | [Ob9GV_UFSZk](https://www.youtube.com/watch?v=Ob9GV_UFSZk) | Daryl Hall &amp; Fitz and the Tantrums - End (Live From Daryl&#x27;s House) |

### E36: #36 - Daryl Hall hosts Neon Trees on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdkAGixSfTYLyjegbJWJw8L

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [v7e-R91eFH4](https://www.youtube.com/watch?v=v7e-R91eFH4) | Daryl Hall &amp; Neon Trees - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [l1kf2Kquuek](https://www.youtube.com/watch?v=l1kf2Kquuek) | Daryl Hall &amp; Neon Trees - Animal (Live From Daryl&#x27;s House) |
| 3 | 3 | [zl-z7xNvyO4](https://www.youtube.com/watch?v=zl-z7xNvyO4) | Daryl Hall &amp; Neon Trees - 1983 (Live From Daryl&#x27;s House) |
| 4 | 4 | [4Dhr9esqSeM](https://www.youtube.com/watch?v=4Dhr9esqSeM) | Daryl Hall &amp; Neon Trees - Love and Affection (Live From Daryl&#x27;s House) |
| 5 | 5 | [jh6NvOJYxeI](https://www.youtube.com/watch?v=jh6NvOJYxeI) | Daryl Hall &amp; Neon Trees - Farther Down (Live From Daryl&#x27;s House) |
| 6 | 6 | [jplg4P3qzg0](https://www.youtube.com/watch?v=jplg4P3qzg0) | Daryl Hall &amp; Neon Trees - Dreams (Fleetwood Mac) (Live From Daryl&#x27;s House) |
| 7 | 7 | [8b89l5ewA5Q](https://www.youtube.com/watch?v=8b89l5ewA5Q) | Daryl Hall &amp; Neon Trees - Head Above Water (Live From Daryl&#x27;s House) |
| 8 | 8 | [A2qabHHq_Z4](https://www.youtube.com/watch?v=A2qabHHq_Z4) | Daryl Hall &amp; Neon Trees - Adult Education (Live From Daryl&#x27;s House) |
| 9 | 9 | [lsoQ5e46fOY](https://www.youtube.com/watch?v=lsoQ5e46fOY) | Daryl Hall &amp; Neon Trees - End (Live From Daryl&#x27;s House) |

### E37: #37 - Daryl Hall hosts Jose Feliciano on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveB3_ynDKJMEEka-0zaDVUM

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [BAd-taWIMZE](https://www.youtube.com/watch?v=BAd-taWIMZE) | Daryl Hall &amp; Jose Feliciano - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [CSN56M1aa0g](https://www.youtube.com/watch?v=CSN56M1aa0g) | Daryl Hall &amp; Jose Feliciano - Fire and Rain (Live From Daryl&#x27;s House) |
| 3 | 3 | [8og2MvZK4lY](https://www.youtube.com/watch?v=8og2MvZK4lY) | Daryl Hall &amp; Jose Feliciano - It Came Upon A Midnight Clear (Live From Daryl&#x27;s House) |
| 4 | 4 | [FiN6TpwWYg4](https://www.youtube.com/watch?v=FiN6TpwWYg4) | Daryl Hall &amp; Jose Feliciano - Christmas Must Be Tonight (Live From Daryl&#x27;s House) |
| 5 | 5 | [7frRzzTPm0M](https://www.youtube.com/watch?v=7frRzzTPm0M) | Daryl Hall &amp; Jose Feliciano - Little Drummer Boy (Live From Daryl&#x27;s House) |
| 6 | 6 | [OMT1xT1fHhA](https://www.youtube.com/watch?v=OMT1xT1fHhA) | Daryl Hall &amp; Jose Feliciano - Light My Fire (Live From Daryl&#x27;s House) |
| 7 | 7 | [gGOoha8QyAU](https://www.youtube.com/watch?v=gGOoha8QyAU) | Daryl Hall &amp; Jose Feliciano - Jingle Bell Rock (Live From Daryl&#x27;s House) |
| 8 | 8 | [HhQyN5Omgo4](https://www.youtube.com/watch?v=HhQyN5Omgo4) | Daryl Hall &amp; Jose Feliciano - Feliz Navidad (Live From Daryl&#x27;s House) |
| 9 | 9 | [MZg5N8q7Uy4](https://www.youtube.com/watch?v=MZg5N8q7Uy4) | Daryl Hall &amp; Jose Feliciano - End (Live From Daryl&#x27;s House) |

### E38: #38 - Daryl Hall hosts Guster on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdJF6zcVcWiJRi191HYtoXI

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [4B4mkBIclVc](https://www.youtube.com/watch?v=4B4mkBIclVc) | Daryl Hall &amp; Guster - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [I9ahYUtIdis](https://www.youtube.com/watch?v=I9ahYUtIdis) | Daryl Hall &amp; Guster - Satellite (Live From Daryl&#x27;s House) |
| 3 | 3 | [OeIlUzma1Cs](https://www.youtube.com/watch?v=OeIlUzma1Cs) | Daryl Hall &amp; Guster - Bad Bad World (Live From Daryl&#x27;s House) |
| 4 | 4 | [O3X0DeB5-7Q](https://www.youtube.com/watch?v=O3X0DeB5-7Q) | Daryl Hall &amp; Guster - Rich Girl (Live From Daryl&#x27;s House) |
| 5 | 5 | [tdNjxN4tg0c](https://www.youtube.com/watch?v=tdNjxN4tg0c) | Daryl Hall &amp; Guster - Do You Love Me (Live From Daryl&#x27;s House) |
| 6 | 6 | [XzyeSfnS6i0](https://www.youtube.com/watch?v=XzyeSfnS6i0) | Daryl Hall &amp; Guster - Hang On (Live From Daryl&#x27;s House) |
| 7 | 7 | [t-fgmGhN09s](https://www.youtube.com/watch?v=t-fgmGhN09s) | Daryl Hall &amp; Guster - Babs and Babs (Live From Daryl&#x27;s House) |
| 8 | 8 | [jNcVcwIJ8G8](https://www.youtube.com/watch?v=jNcVcwIJ8G8) | Daryl Hall &amp; Guster - End (Live From Daryl&#x27;s House) |

### E39: #39 - New Years Eve Special on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveyLJaQUV5Zvzxffg5YpJ8C

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [hdjNEGWDQFA](https://www.youtube.com/watch?v=hdjNEGWDQFA) | Daryl Hall - New Year&#x27;s Eve Special - Rob Thomas - Kiss On My List (Live From Daryl&#x27;s House) |
| 2 | 2 | [fTkm9282bh8](https://www.youtube.com/watch?v=fTkm9282bh8) | Daryl Hall - New Year&#x27;s Eve Special - Neon Trees - Animal (Live From Daryl&#x27;s House) |
| 3 | 3 | [y4gCUciM3Tc](https://www.youtube.com/watch?v=y4gCUciM3Tc) | Daryl Hall - New Year&#x27;s Eve Special - Train - Hey Soul Sister (Live From Daryl&#x27;s House) |
| 4 | 4 | [Eln2Z7HbYGs](https://www.youtube.com/watch?v=Eln2Z7HbYGs) | Sharon Jones - Gotta Thing On My Mind (Live From Daryl&#x27;s House - New Year&#x27;s Eve Special) |
| 5 | 5 | [Zo7ZC1Bqlh4](https://www.youtube.com/watch?v=Zo7ZC1Bqlh4) | Daryl Hall - New Year&#x27;s Eve Special - Eli &#x27;Paperboy&#x27; Reed - Pick A Number (Live From Daryl&#x27;s House) |
| 6 | 6 | [fcrewPbP14U](https://www.youtube.com/watch?v=fcrewPbP14U) | Smokey Robinson - Sara Smile / Ooh Baby Baby (Live From Daryl&#x27;s House - New Year&#x27;s Eve Special) |
| 7 | 7 | [BRmBg0DyOSg](https://www.youtube.com/watch?v=BRmBg0DyOSg) | Daryl Hall - New Year&#x27;s Eve Special - Todd Rundgren - The Want Of A Nail (Live From Daryl&#x27;s House) |
| 8 | 8 | [yJkg06ETPAA](https://www.youtube.com/watch?v=yJkg06ETPAA) | Daryl Hall - New Year&#x27;s Eve Special - Patrick Stump - What A Catch, Donnie (Live From Daryl&#x27;s House) |
| 9 | 9 | [jt33NL2xfYA](https://www.youtube.com/watch?v=jt33NL2xfYA) | Toots &amp; The Maytals - Reggae Got Soul (Live From Daryl&#x27;s House - New Year&#x27;s Eve Special) |
| 10 | 10 | [JrSf84ZmcWc](https://www.youtube.com/watch?v=JrSf84ZmcWc) | Fitz &amp; The Tantrums - Breakin&#x27; The Chains of Love (Live From Daryl&#x27;s House - New Year&#x27;s Eve Special) |
| 11 | 11 | [sfSzzL2jifo](https://www.youtube.com/watch?v=sfSzzL2jifo) | Daryl Hall - New Year&#x27;s Eve Special - Train - Wait For Me (Live From Daryl&#x27;s House) |
| 12 | 12 | [-OWwZbilYEU](https://www.youtube.com/watch?v=-OWwZbilYEU) | Daryl Hall - New Year&#x27;s Eve Special - Jose Feliciano - Feliz Navidad (Live From Daryl&#x27;s House) |

### E40: #40 - Daryl Hall hosts Todd Rundgren on Live From Daryl&#x27;s House in Hawaii

https://www.youtube.com/playlist?list=PLINSQGXREtvckRDkC3dG4f-EVTHfa041G

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-V9BnimZkP0](https://www.youtube.com/watch?v=-V9BnimZkP0) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [CIcKW1RBGK0](https://www.youtube.com/watch?v=CIcKW1RBGK0) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - The Last Ride (Live From Daryl&#x27;s House Special) |
| 3 | 3 | [x_yzYulh5bc](https://www.youtube.com/watch?v=x_yzYulh5bc) | Todd Rundgren - Beanie G and The Rose Tattoo (Live From Daryl&#x27;s House - Hawai&#x27;i Special) |
| 4 | 4 | [H5XmQqPmi6Y](https://www.youtube.com/watch?v=H5XmQqPmi6Y) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - I Saw The Light (Live From Daryl&#x27;s House Special) |
| 5 | 5 | [x_wR6_AX_qs](https://www.youtube.com/watch?v=x_wR6_AX_qs) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - Ending and Credits Part 1 (Live From Daryl&#x27;s House) |
| 6 | 6 | [OFsYdqP7CR4](https://www.youtube.com/watch?v=OFsYdqP7CR4) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - Production / Intro Part 2 (Live From Daryl&#x27;s House) |
| 7 | 7 | [5M-Y1pN7xZQ](https://www.youtube.com/watch?v=5M-Y1pN7xZQ) | Todd Rundgren - Didn&#x27;t I (Blow Your Mind This Time) (Live From Daryl&#x27;s House - Hawai&#x27;i Special) |
| 8 | 8 | [B9sEf3enReM](https://www.youtube.com/watch?v=B9sEf3enReM) | Todd Rundgren - It Wouldn&#x27;t Have Made Any Difference (Live From Daryl&#x27;s House - Hawai&#x27;i Special) |
| 9 | 9 | [2ChAAlfRTgI](https://www.youtube.com/watch?v=2ChAAlfRTgI) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - Bang the Drum All Day (Live From Daryl&#x27;s House Special) |
| 10 | 10 | [SW7d777852k](https://www.youtube.com/watch?v=SW7d777852k) | Daryl Hall &amp; Todd Rundgren in Hawai&#x27;i - Ending and Credits Part 2 (Live From Daryl&#x27;s House) |

### E41: #41 - Daryl Hall hosts Dave Stewart of Eurythmics on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcx4eZQXJFedgzZTUAZ7SwF

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [XYQYE3mcN90](https://www.youtube.com/watch?v=XYQYE3mcN90) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [xdZnjWC2BwU](https://www.youtube.com/watch?v=xdZnjWC2BwU) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Magic In The Blues (Live From Daryl&#x27;s House) |
| 3 | 3 | [w_9A3AhRf0E](https://www.youtube.com/watch?v=w_9A3AhRf0E) | Daryl Hall &amp; Dave Stewart (Eurythmics) - The Gypsy Girl and Me (Live From Daryl&#x27;s House) |
| 4 | 4 | [R0RfU8hCjPo](https://www.youtube.com/watch?v=R0RfU8hCjPo) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Dreamtime (Live From Daryl&#x27;s House) |
| 5 | 5 | [1JYBnKPGIxU](https://www.youtube.com/watch?v=1JYBnKPGIxU) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Heart of Stone (Live From Daryl&#x27;s House) |
| 6 | 6 | [UEpgFvtizyc](https://www.youtube.com/watch?v=UEpgFvtizyc) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Missionary Man (Live From Daryl&#x27;s House) |
| 7 | 7 | [cUcdAxoRLyY](https://www.youtube.com/watch?v=cUcdAxoRLyY) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Worth The Waiting For (Live From Daryl&#x27;s House) |
| 8 | 8 | [1ASqiVJOLpI](https://www.youtube.com/watch?v=1ASqiVJOLpI) | Daryl Hall &amp; Dave Stewart (Eurythmics) - Here Comes The Rain Again (Live From Daryl&#x27;s House) |
| 9 | 9 | [4NhOoRyuMIA](https://www.youtube.com/watch?v=4NhOoRyuMIA) | Daryl Hall &amp; Dave Stewart (Eurythmics) - End (Live From Daryl&#x27;s House) |

### E42: #42 - Daryl Hall hosts John Rzeznik of Goo Goo Dolls on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvczXcIq4QePBkvLUC85agfG

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Uob-tMS6iDk](https://www.youtube.com/watch?v=Uob-tMS6iDk) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [FjyX4vR8fcg](https://www.youtube.com/watch?v=FjyX4vR8fcg) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Slide (Live From Daryl&#x27;s House) |
| 3 | 3 | [JgNuIuRbf28](https://www.youtube.com/watch?v=JgNuIuRbf28) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Home (Live From Daryl&#x27;s House) |
| 4 | 4 | [_chBq4Jtdv0](https://www.youtube.com/watch?v=_chBq4Jtdv0) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Still Your Song (Live From Daryl&#x27;s House) |
| 5 | 5 | [LVeTgFoPnug](https://www.youtube.com/watch?v=LVeTgFoPnug) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Did It In A Minute (Live From Daryl&#x27;s House) |
| 6 | 6 | [mQhghn1r7g8](https://www.youtube.com/watch?v=mQhghn1r7g8) | Daryl Hall &amp; John Rzeznik - Some Things Are Better Left Unsaid (Live From Daryl&#x27;s House) |
| 7 | 7 | [SDoKVIXIJJc](https://www.youtube.com/watch?v=SDoKVIXIJJc) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Want To (Live From Daryl&#x27;s House) |
| 8 | 8 | [PPlg6aSFzg0](https://www.youtube.com/watch?v=PPlg6aSFzg0) | Daryl Hall &amp; John Rzeznik (Goo Goo Dolls) - Iris (Live From Daryl&#x27;s House) |

### E43: #43 - Daryl Hall hosts Mayer Hawthorne on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcYMNrWP1AN0JQ4gYblg2KW

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [44RiG7MHKHg](https://www.youtube.com/watch?v=44RiG7MHKHg) | Daryl Hall &amp; Mayer Hawthorne - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [YYif7GZvY2I](https://www.youtube.com/watch?v=YYif7GZvY2I) | Daryl Hall &amp; Mayer Hawthorne - Strange Arrangement (Live From Daryl&#x27;s House) |
| 3 | 3 | [scVkLiYzDEI](https://www.youtube.com/watch?v=scVkLiYzDEI) | Daryl Hall &amp; Mayer Hawthorne - No Strings (Live From Daryl&#x27;s House) |
| 4 | 4 | [G9emA-sNC9U](https://www.youtube.com/watch?v=G9emA-sNC9U) | Daryl Hall &amp; Mayer Hawthorne - You Make My Dreams (Live From Daryl&#x27;s House) |
| 5 | 5 | [8fbNg6TayWI](https://www.youtube.com/watch?v=8fbNg6TayWI) | Daryl Hall &amp; Mayer Hawthorne - Just Ain&#x27;t Gonna Work Out (Live From Daryl&#x27;s House) |
| 6 | 6 | [t3Z3oDp_BVg](https://www.youtube.com/watch?v=t3Z3oDp_BVg) | Daryl Hall &amp; Mayer Hawthorne - Your Easy Lovin&#x27; Ain&#x27;t Pleasin&#x27; Nothin&#x27; (Live From Daryl&#x27;s House) |
| 7 | 7 | [mrIyI74NH6M](https://www.youtube.com/watch?v=mrIyI74NH6M) | Daryl Hall &amp; Mayer Hawthorne - Private Eyes (Live From Daryl&#x27;s House) |
| 8 | 8 | [90hnpE6o95g](https://www.youtube.com/watch?v=90hnpE6o95g) | Daryl Hall &amp; Mayer Hawthorne - End (Live From Daryl&#x27;s House) |

### E44: #44 - Daryl Hall hosts Booker T. Jones on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvf6asN95rllRtPTDms4Cu1K

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [6VaJuw2vxHI](https://www.youtube.com/watch?v=6VaJuw2vxHI) | Daryl Hall &amp; Booker T. Jones (Booker T. &amp; the M.G.&#x27;s) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [u-bC_DjJMo4](https://www.youtube.com/watch?v=u-bC_DjJMo4) | Daryl Hall &amp; Booker T. Jones (Booker T. &amp; the M.G.&#x27;s) - Down In Memphis (Live From Daryl&#x27;s House) |
| 3 | 3 | [i4HmAcvI74A](https://www.youtube.com/watch?v=i4HmAcvI74A) | Daryl Hall &amp; Booker T. Jones (Booker T. &amp; the M.G.&#x27;s) - Green Onions (Live From Daryl&#x27;s House) |
| 4 | 4 | [3HlgMsVl_80](https://www.youtube.com/watch?v=3HlgMsVl_80) | Daryl Hall &amp; Booker T. Jones (Booker T. &amp; the M.G.&#x27;s) - Never Found A Girl (Live From Daryl&#x27;s House) |
| 5 | 5 | [B4gfyDqE9nQ](https://www.youtube.com/watch?v=B4gfyDqE9nQ) | Daryl Hall &amp; Booker T. Jones - Everyday Will Be Like A Holiday |
| 6 | 6 | [bR_IR0-UFg8](https://www.youtube.com/watch?v=bR_IR0-UFg8) | Daryl Hall &amp; Booker T. Jones - Born Under A Bad Sign (Live From Daryl&#x27;s House) |
| 7 | 7 | [Kn0W38HoY_E](https://www.youtube.com/watch?v=Kn0W38HoY_E) | Daryl Hall &amp; Booker T. Jones - I Can&#x27;t Go For That (No Can Do) (Live From Daryl&#x27;s House) |
| 8 | 8 | [gf2Lh5f2evQ](https://www.youtube.com/watch?v=gf2Lh5f2evQ) | Daryl Hall &amp; Booker T. Jones (Booker T. &amp; the M.G.&#x27;s) - End (Live From Daryl&#x27;s House) |

### E45: #45 - Daryl Hall hosts Grace Potter on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfKbU3sg39y2E0c6xYGi3XQ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [SXuv89X_3VM](https://www.youtube.com/watch?v=SXuv89X_3VM) | Daryl Hall &amp; Grace Potter - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [PBj95muvtOk](https://www.youtube.com/watch?v=PBj95muvtOk) | Daryl Hall &amp; Grace Potter - Low Road (Live From Daryl&#x27;s House) |
| 3 | 3 | [jVlkYiwC4Ng](https://www.youtube.com/watch?v=jVlkYiwC4Ng) | Daryl Hall &amp; Grace Potter - Money (Live From Daryl&#x27;s House) |
| 4 | 4 | [J19Qy9WtN_w](https://www.youtube.com/watch?v=J19Qy9WtN_w) | Daryl Hall &amp; Grace Potter - Things I Never Needed (Live From Daryl&#x27;s House) |
| 5 | 5 | [EpJHYI-uuwA](https://www.youtube.com/watch?v=EpJHYI-uuwA) | Daryl Hall &amp; Grace Potter - Room To Breathe (Live From Daryl&#x27;s House) |
| 6 | 6 | [k1ESe7J-VDg](https://www.youtube.com/watch?v=k1ESe7J-VDg) | Daryl Hall &amp; Grace Potter - Goodbye Kiss (Live From Daryl&#x27;s House) |
| 7 | 7 | [6HidKdc0IWs](https://www.youtube.com/watch?v=6HidKdc0IWs) | Daryl Hall &amp; Grace Potter - Paris (Ooh La La) (Live From Daryl&#x27;s House) |
| 8 | 8 | [mn_Ktxs5cpA](https://www.youtube.com/watch?v=mn_Ktxs5cpA) | Daryl Hall &amp; Grace Potter - End (Live From Daryl&#x27;s House) |

### E46: #46 - Daryl Hall hosts Nikki Jean on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc5X_Jj8lTmhW_iWJX8KD-b

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [dbLCm5SASgI](https://www.youtube.com/watch?v=dbLCm5SASgI) | Daryl Hall &amp; Nikki Jean - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [nnCwQ7SGnXE](https://www.youtube.com/watch?v=nnCwQ7SGnXE) | Daryl Hall &amp; Nikki Jean - Sex Lies And Sunshine (Live From Daryl&#x27;s House) |
| 3 | 3 | [KMVNz8XVs_4](https://www.youtube.com/watch?v=KMVNz8XVs_4) | Daryl Hall &amp; Nikki Jean - Bio (Live From Daryl&#x27;s House) |
| 4 | 4 | [aybzAae8FOY](https://www.youtube.com/watch?v=aybzAae8FOY) | Daryl Hall &amp; Nikki Jean - How To UnRing A Bell (Live From Daryl&#x27;s House) |
| 5 | 5 | [1NofABKO6iU](https://www.youtube.com/watch?v=1NofABKO6iU) | Daryl Hall &amp; Nikki Jean - My Love (Live From Daryl&#x27;s House) |
| 6 | 6 | [xWHAsL0tCOE](https://www.youtube.com/watch?v=xWHAsL0tCOE) | Daryl Hall &amp; Nikki Jean - Cookie Social (Live From Daryl&#x27;s House) |
| 7 | 7 | [OMTaE6IIONs](https://www.youtube.com/watch?v=OMTaE6IIONs) | Daryl Hall &amp; Nikki Jean - One On One (Live From Daryl&#x27;s House) |
| 8 | 8 | [pS790XN3Gc0](https://www.youtube.com/watch?v=pS790XN3Gc0) | Daryl Hall &amp; Nikki Jean - Bob Dylan (Live From Daryl&#x27;s House) |
| 9 | 9 | [KEq7n5PRTXk](https://www.youtube.com/watch?v=KEq7n5PRTXk) | Daryl Hall &amp; Nikki Jean - Steel and Feathers (Live From Daryl&#x27;s House) |
| 10 | 10 | [9oapsL2qzU4](https://www.youtube.com/watch?v=9oapsL2qzU4) | Daryl Hall &amp; Nikki Jean - Patty Crash (Intro) (Live From Daryl&#x27;s House) |
| 11 | 11 | [QihexSoUnZE](https://www.youtube.com/watch?v=QihexSoUnZE) | Daryl Hall &amp; Nikki Jean - Patty Crash (Live From Daryl&#x27;s House) |
| 12 | 12 | [rOVKIO5IYxk](https://www.youtube.com/watch?v=rOVKIO5IYxk) | Daryl Hall &amp; Nikki Jean - Dinner (Live From Daryl&#x27;s House) |
| 13 | 13 | [Vignc0dBLIo](https://www.youtube.com/watch?v=Vignc0dBLIo) | Daryl Hall &amp; Nikki Jean - My Mistake (Live From Daryl&#x27;s House) |
| 14 | 14 | [EUEgUtD-STc](https://www.youtube.com/watch?v=EUEgUtD-STc) | Daryl Hall &amp; Nikki Jean - End (Live From Daryl&#x27;s House) |

### E47: #47 - Daryl Hall Performs &quot;Laughing Down Crying&quot; Part 1

https://www.youtube.com/playlist?list=PLINSQGXREtvdPi8LsxG2rQOOzL_VCOf8z

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [fZhpukyjuuk](https://www.youtube.com/watch?v=fZhpukyjuuk) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [Ka6gPfSCTVY](https://www.youtube.com/watch?v=Ka6gPfSCTVY) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Laughing Down Crying (Live From Daryl&#x27;s House) |
| 3 | 3 | [uFSfiXr6YXE](https://www.youtube.com/watch?v=uFSfiXr6YXE) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Talking to You (Live From Daryl&#x27;s House) |
| 4 | 4 | [9zCxFiGdvkQ](https://www.youtube.com/watch?v=9zCxFiGdvkQ) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Lifetime Of Love (Live From Daryl&#x27;s House) |
| 5 | 5 | [5SUv3VPEX90](https://www.youtube.com/watch?v=5SUv3VPEX90) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Eyes For You (Live From Daryl&#x27;s House) |
| 6 | 6 | [oItMdcw1BuE](https://www.youtube.com/watch?v=oItMdcw1BuE) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - Save Me (Live From Daryl&#x27;s House) |
| 7 | 7 | [B7bN_Upl46I](https://www.youtube.com/watch?v=B7bN_Upl46I) | Daryl Hall &quot;Laughing Down Crying&quot; Part 1 - End (Live From Daryl&#x27;s House) |

### E48: #48 - Daryl Hall Performs &quot;Laughing Down Crying&quot; Part 2

https://www.youtube.com/playlist?list=PLINSQGXREtvdUY8ofO6Ig5GvG2uiYKFFJ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [KJ33Irpp_kM](https://www.youtube.com/watch?v=KJ33Irpp_kM) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [KCbRY-WpkOo](https://www.youtube.com/watch?v=KCbRY-WpkOo) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - Message To Ya (Live From Daryl&#x27;s House) |
| 3 | 3 | [a3jB9SkoLfU](https://www.youtube.com/watch?v=a3jB9SkoLfU) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - Get Out Of The Way (Live From Daryl&#x27;s House) |
| 4 | 4 | [gZCB8dNK_PM](https://www.youtube.com/watch?v=gZCB8dNK_PM) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2  - Wrong Side Of History (Live From Daryl&#x27;s House) |
| 5 | 5 | [X-TUOULTxso](https://www.youtube.com/watch?v=X-TUOULTxso) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - Crash And Burn (Live From Daryl&#x27;s House) |
| 6 | 6 | [5-GPiZWO5R0](https://www.youtube.com/watch?v=5-GPiZWO5R0) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - Problem With You (Live From Daryl&#x27;s House) |
| 7 | 7 | [UCpwlX7m8Og](https://www.youtube.com/watch?v=UCpwlX7m8Og) | Daryl Hall &quot;Laughing Down Crying&quot; Part 2 - End (Live From Daryl&#x27;s House) |

### E49: #49 - Daryl Hall hosts Blind Boys of Alabama on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdrLNdNtIHPYYST1kh7M3fJ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [r0hJZ3jpcEQ](https://www.youtube.com/watch?v=r0hJZ3jpcEQ) | Daryl Hall &amp; The Blind Boys of Alabama - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [2zkxwHgmgQU](https://www.youtube.com/watch?v=2zkxwHgmgQU) | Daryl Hall &amp; The Blind Boys of Alabama - Take The High Road (Live From Daryl&#x27;s House) |
| 3 | 3 | [fufL3GGp160](https://www.youtube.com/watch?v=fufL3GGp160) | Daryl Hall &amp; The Blind Boys of Alabama - Born In Bethlehem (Live From Daryl&#x27;s House) |
| 4 | 4 | [Flw2-U5g_Ik](https://www.youtube.com/watch?v=Flw2-U5g_Ik) | Daryl Hall &amp; The Blind Boys of Alabama - Midnight Clear (Live From Daryl&#x27;s House) |
| 5 | 5 | [8tydxIV7tFA](https://www.youtube.com/watch?v=8tydxIV7tFA) | Daryl Hall &amp; The Blind Boys of Alabama - Go Tell It On The Mountain (Live From Daryl&#x27;s House) |
| 6 | 6 | [_VnZRCJ1DoU](https://www.youtube.com/watch?v=_VnZRCJ1DoU) | Daryl Hall &amp; The Blind Boys of Alabama - Can You Give Me A Drink (Live From Daryl&#x27;s House) |
| 7 | 7 | [T84rsmJVgaM](https://www.youtube.com/watch?v=T84rsmJVgaM) | Daryl Hall &amp; The Blind Boys of Alabama - Last Month of The Year (Live From Daryl&#x27;s House) |
| 8 | 8 | [VxPhWXe2_FQ](https://www.youtube.com/watch?v=VxPhWXe2_FQ) | Daryl Hall &amp; The Blind Boys of Alabama - End (Live From Daryl&#x27;s House) |

### E50: #50 - Daryl Hall hosts Keb&#x27; Mo&#x27; on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveU9ewvOExoXNvdMWPo83NV

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [UuDH7Dit8qc](https://www.youtube.com/watch?v=UuDH7Dit8qc) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [yUX-yZH61P0](https://www.youtube.com/watch?v=yUX-yZH61P0) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - The Whole Enchilada (Live From Daryl&#x27;s House) |
| 3 | 3 | [M8KZV2ZeyKo](https://www.youtube.com/watch?v=M8KZV2ZeyKo) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - All The Way (Live From Daryl&#x27;s House) |
| 4 | 4 | [nICe9ZBkAIM](https://www.youtube.com/watch?v=nICe9ZBkAIM) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - Inside Outside (Live From Daryl&#x27;s House) |
| 5 | 5 | [91NaRFskge4](https://www.youtube.com/watch?v=91NaRFskge4) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - Everything Your Heart Desires (Live From Daryl&#x27;s House) |
| 6 | 6 | [cHedZ4ePUi0](https://www.youtube.com/watch?v=cHedZ4ePUi0) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - My Baby Is Telling Lies Again (Live From Daryl&#x27;s House) |
| 7 | 7 | [QVVosvKAu9k](https://www.youtube.com/watch?v=QVVosvKAu9k) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - We Don&#x27;t Need It (Live From Daryl&#x27;s House) |
| 8 | 8 | [P5-5nFflDYM](https://www.youtube.com/watch?v=P5-5nFflDYM) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - Cab Driver (Live From Daryl&#x27;s House) |
| 9 | 9 | [VjAy_eziHXc](https://www.youtube.com/watch?v=VjAy_eziHXc) | Daryl Hall &amp; Keb&#x27; Mo&#x27; - End (Live From Daryl&#x27;s House) |

### E51: #51 - Daryl Hall hosts Allen Stone on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdxN7Zp-TbPiN6jTECbXWP8

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Ti8WjyuguTw](https://www.youtube.com/watch?v=Ti8WjyuguTw) | Daryl Hall &amp; Allen Stone - LFDH nu Soul Revue Tour (Live From Daryl&#x27;s House) |
| 2 | 2 | [zK171X4xM74](https://www.youtube.com/watch?v=zK171X4xM74) | Daryl Hall &amp; Allen Stone - Intro (Live From Daryl&#x27;s House) |
| 3 | 3 | [g7ssl3DEqbM](https://www.youtube.com/watch?v=g7ssl3DEqbM) | Daryl Hall &amp; Allen Stone - Celebrate Tonight (Live From Daryl&#x27;s House) |
| 4 | 4 | [sxx4TaglIDA](https://www.youtube.com/watch?v=sxx4TaglIDA) | Daryl Hall &amp; Allen Stone - Interview (Live From Daryl&#x27;s House) |
| 5 | 5 | [daGCTalHjnY](https://www.youtube.com/watch?v=daGCTalHjnY) | Daryl Hall &amp; Allen Stone - What I&#x27;ve Seen (Live From Daryl&#x27;s House) |
| 6 | 6 | [lS4wm4H9xVI](https://www.youtube.com/watch?v=lS4wm4H9xVI) | Daryl Hall &amp; Allen Stone - Food Prep (Live From Daryl&#x27;s House) |
| 7 | 7 | [WUB8OzBnEaA](https://www.youtube.com/watch?v=WUB8OzBnEaA) | Daryl Hall &amp; Allen Stone - Unaware (Live From Daryl&#x27;s House) |
| 8 | 8 | [YGRYTfPL9h8](https://www.youtube.com/watch?v=YGRYTfPL9h8) | Daryl Hall &amp; Allen Stone - Dinner (Live From Daryl&#x27;s House) |
| 9 | 9 | [7ARyIucwOFQ](https://www.youtube.com/watch?v=7ARyIucwOFQ) | Daryl Hall &amp; Allen Stone - Say So (Live From Daryl&#x27;s House) |
| 10 | 10 | [--7cYhaLUnE](https://www.youtube.com/watch?v=--7cYhaLUnE) | Daryl Hall &amp; Allen Stone - Drummer Brian Breaks His Foot (Live From Daryl&#x27;s House) |
| 11 | 11 | [L4g2exSa2p0](https://www.youtube.com/watch?v=L4g2exSa2p0) | Daryl Hall &amp; Allen Stone - Lifetime of Love (Live From Daryl&#x27;s House) |
| 12 | 12 | [C0i-Kzee_gc](https://www.youtube.com/watch?v=C0i-Kzee_gc) | Daryl Hall &amp; Allen Stone - Ennui On The Mountain (Live From Daryl&#x27;s House) |
| 13 | 13 | [Hd_3XuZ7tGg](https://www.youtube.com/watch?v=Hd_3XuZ7tGg) | Daryl Hall &amp; Allen Stone - End (Live From Daryl&#x27;s House) |

### E52: #52 - Daryl Hall hosts CeeLo Green on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfY1kC4iUXLirBbTpvGOzaC

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [CefJDcOexMU](https://www.youtube.com/watch?v=CefJDcOexMU) | Daryl Hall &amp; CeeLo Green - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [7rN9fqCRoUw](https://www.youtube.com/watch?v=7rN9fqCRoUw) | Daryl Hall &amp; CeeLo Green - Bright Lights Bigger City (Live From Daryl&#x27;s House) |
| 3 | 3 | [CZoNRtcT7bc](https://www.youtube.com/watch?v=CZoNRtcT7bc) | Daryl Hall &amp; CeeLo Green - Crazy (Live From Daryl&#x27;s House) |
| 4 | 4 | [d0N_3Zz3jjY](https://www.youtube.com/watch?v=d0N_3Zz3jjY) | Daryl Hall &amp; CeeLo Green - Forget You (Live From Daryl&#x27;s House) |
| 5 | 5 | [PmDw7BRE_VY](https://www.youtube.com/watch?v=PmDw7BRE_VY) | Daryl Hall &amp; CeeLo Green - F*ck You (Live From Daryl&#x27;s House) |
| 6 | 6 | [bi6qwU_eFEo](https://www.youtube.com/watch?v=bi6qwU_eFEo) | Daryl Hall &amp; CeeLo Green - Cry Baby (Live From Daryl&#x27;s House) |
| 7 | 7 | [TRwZD7MpAow](https://www.youtube.com/watch?v=TRwZD7MpAow) | Daryl Hall &amp; CeeLo Green - One On One (Live From Daryl&#x27;s House) |
| 8 | 8 | [fSEm7ju8Ruo](https://www.youtube.com/watch?v=fSEm7ju8Ruo) | Daryl Hall &amp; CeeLo Green - I Can&#x27;t Go For That (No Can Do) (Live From Daryl&#x27;s House) |
| 9 | 9 | [wfWEcTl7w7s](https://www.youtube.com/watch?v=wfWEcTl7w7s) | Daryl Hall &amp; CeeLo Green - End (Live From Daryl&#x27;s House) |

### E53: #53 - Daryl Hall hosts Dirty Heads on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvekHd-GuiByzm25w7KK1jwJ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [u_8gcRr1dS0](https://www.youtube.com/watch?v=u_8gcRr1dS0) | Daryl Hall &amp; The Dirty Heads - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [eeCSWlnHS8g](https://www.youtube.com/watch?v=eeCSWlnHS8g) | Daryl Hall &amp; The Dirty Heads - Spread Too Thin (Live From Daryl&#x27;s House) |
| 3 | 3 | [5MB0KjC4q_8](https://www.youtube.com/watch?v=5MB0KjC4q_8) | Daryl Hall &amp; The Dirty Heads - Cooking (Live From Daryl&#x27;s House) |
| 4 | 4 | [w9IGf6GdLIQ](https://www.youtube.com/watch?v=w9IGf6GdLIQ) | Daryl Hall &amp; The Dirty Heads - Cabin By The Sea (Live From Daryl&#x27;s House) |
| 5 | 5 | [6qcL9yVD3eI](https://www.youtube.com/watch?v=6qcL9yVD3eI) | Daryl Hall &amp; The Dirty Heads - Lay Me Down (Live From Daryl&#x27;s House) |
| 6 | 6 | [9HFDG5kLk-A](https://www.youtube.com/watch?v=9HFDG5kLk-A) | Daryl Hall &amp; The Dirty Heads - Dinner Part 1 (Live From Daryl&#x27;s House) |
| 7 | 7 | [dcqcSJ1YGV8](https://www.youtube.com/watch?v=dcqcSJ1YGV8) | Daryl Hall &amp; The Dirty Heads - Stand Tall (Live From Daryl&#x27;s House) |
| 8 | 8 | [uFwzsLjyNI8](https://www.youtube.com/watch?v=uFwzsLjyNI8) | Daryl Hall &amp; The Dirty Heads - Dinner Part 2 (Live From Daryl&#x27;s House) |
| 9 | 9 | [sgNhB3kXhXw](https://www.youtube.com/watch?v=sgNhB3kXhXw) | Daryl Hall &amp; The Dirty Heads - Send Me (Live From Daryl&#x27;s House) |
| 10 | 10 | [WlsfFwI4YBA](https://www.youtube.com/watch?v=WlsfFwI4YBA) | Daryl Hall &amp; The Dirty Heads - Rich Girl (Live From Daryl&#x27;s House) |
| 11 | 11 | [xL1zN-5Q1sw](https://www.youtube.com/watch?v=xL1zN-5Q1sw) | Daryl Hall &amp; The Dirty Heads - End (Live From Daryl&#x27;s House) |

### E54: #54 - Daryl Hall hosts Butch Walker on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcLROJJSnX996n6gMP1-u4x

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [ZrZXNoBZEso](https://www.youtube.com/watch?v=ZrZXNoBZEso) | Daryl Hall &amp; Butch Walker - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [SnwZv6fJPu0](https://www.youtube.com/watch?v=SnwZv6fJPu0) | Daryl Hall &amp; Butch Walker - Bodegas and Blood (Live From Daryl&#x27;s House) |
| 3 | 3 | [ZgUWvIaLn2o](https://www.youtube.com/watch?v=ZgUWvIaLn2o) | Daryl Hall &amp; Butch Walker - Interview (Live From Daryl&#x27;s House) |
| 4 | 4 | [5lhCwtfm9Jc](https://www.youtube.com/watch?v=5lhCwtfm9Jc) | Daryl Hall &amp; Butch Walker - Sweethearts (Live From Daryl&#x27;s House) |
| 5 | 5 | [Qy_0Xh6Scmg](https://www.youtube.com/watch?v=Qy_0Xh6Scmg) | Daryl Hall &amp; Butch Walker - Cooking (Live From Daryl&#x27;s House) |
| 6 | 6 | [XZvnWqsxcJk](https://www.youtube.com/watch?v=XZvnWqsxcJk) | Daryl Hall &amp; Butch Walker - Closest Thing (Live From Daryl&#x27;s House) |
| 7 | 7 | [FXygaO86Orc](https://www.youtube.com/watch?v=FXygaO86Orc) | Daryl Hall &amp; Butch Walker - Dinner (Live From Daryl&#x27;s House) |
| 8 | 8 | [hSF2k49njxQ](https://www.youtube.com/watch?v=hSF2k49njxQ) | Daryl Hall &amp; Butch Walker - Mixtape (Live From Daryl&#x27;s House) |
| 9 | 9 | [m43HleBGz0A](https://www.youtube.com/watch?v=m43HleBGz0A) | Daryl Hall &amp; Butch Walker - Dinner Part 2 (Live From Daryl&#x27;s House) |
| 10 | 10 | [II3HoQDiq-A](https://www.youtube.com/watch?v=II3HoQDiq-A) | Daryl Hall &amp; Butch Walker - Why Was It So Easy (Live From Daryl&#x27;s House) |
| 11 | 11 | [Hbvdcb-wiQw](https://www.youtube.com/watch?v=Hbvdcb-wiQw) | Daryl Hall &amp; Butch Walker - Say It Isn&#x27;t So (Live From Daryl&#x27;s House) |
| 12 | 12 | [hPDkPwMWTlc](https://www.youtube.com/watch?v=hPDkPwMWTlc) | Daryl Hall &amp; Butch Walker - End (Live From Daryl&#x27;s House) |

### E55: #55 - Daryl Hall hosts Jason Mraz on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfZILRE6ej6ZuXMpJe30Dvg

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [64eYLEGySUE](https://www.youtube.com/watch?v=64eYLEGySUE) | Daryl Hall &amp; Jason Mraz - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [Q2dzWR_dCYg](https://www.youtube.com/watch?v=Q2dzWR_dCYg) | Daryl Hall &amp; Jason Mraz - The Remedy (Live From Daryl&#x27;s House) |
| 3 | 3 | [kUeWdYyQfTQ](https://www.youtube.com/watch?v=kUeWdYyQfTQ) | Daryl Hall &amp; Jason Mraz - I Won&#x27;t Give Up (Live From Daryl&#x27;s House) |
| 4 | 4 | [SkVkOYxp440](https://www.youtube.com/watch?v=SkVkOYxp440) | Daryl Hall &amp; Jason Mraz - So Close (Live From Daryl&#x27;s House) |
| 5 | 5 | [q1YqnNyGDFM](https://www.youtube.com/watch?v=q1YqnNyGDFM) | Daryl Hall &amp; Jason Mraz - I&#x27;m Yours (Live From Daryl&#x27;s House) |
| 6 | 6 | [PmL84_iw7RA](https://www.youtube.com/watch?v=PmL84_iw7RA) | Daryl Hall &amp; Jason Mraz - Eyes for You (Ain&#x27;t No Doubt About It) (Live From Daryl&#x27;s House) |
| 7 | 7 | [CzPg_A6rU6A](https://www.youtube.com/watch?v=CzPg_A6rU6A) | Daryl Hall &amp; Jason Mraz - 93 Million Miles (Live From Daryl&#x27;s House) |

### E56: #56 - Daryl Hall hosts Chiddy Bang on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvehk-2P6RK0nJRREH3joeVc

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [YydhHC55rxI](https://www.youtube.com/watch?v=YydhHC55rxI) | Daryl Hall &amp; Chiddy Bang - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [MK-VLshtoBo](https://www.youtube.com/watch?v=MK-VLshtoBo) | Daryl Hall &amp; Chiddy Bang - Opposite Of Adults (Live From Daryl&#x27;s House) |
| 3 | 3 | [_rUeTXoF2m4](https://www.youtube.com/watch?v=_rUeTXoF2m4) | Daryl Hall &amp; Chiddy Bang - Ray Charles (Live From Daryl&#x27;s House) |
| 4 | 4 | [_LN1GxX6QsA](https://www.youtube.com/watch?v=_LN1GxX6QsA) | Daryl Hall &amp; Chiddy Bang - Mind Your Manners (Live From Daryl&#x27;s House) |
| 5 | 5 | [TD7BycCHq5o](https://www.youtube.com/watch?v=TD7BycCHq5o) | Daryl Hall &amp; Chiddy Bang - Take You Back ft. Frank Stallone (Live From Daryl&#x27;s House) |
| 6 | 6 | [dmaQcGFKiHA](https://www.youtube.com/watch?v=dmaQcGFKiHA) | Daryl Hall &amp; Chiddy Bang - Fall In Philadelphia (Live From Daryl&#x27;s House) |
| 7 | 7 | [gv0l-AdIXq0](https://www.youtube.com/watch?v=gv0l-AdIXq0) | Daryl Hall &amp; Chiddy Bang - Talking To Myself (Live From Daryl&#x27;s House) |
| 8 | 8 | [2TQzo__oryw](https://www.youtube.com/watch?v=2TQzo__oryw) | Daryl Hall &amp; Chiddy Bang - She Got Me Bad (Live From Daryl&#x27;s House) |

### E57: #57 - Daryl Hall hosts Rumer on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdpFq6iW-3VIcibf3g4rc13

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-2nIEWUd1oA](https://www.youtube.com/watch?v=-2nIEWUd1oA) | Daryl Hall &amp; Rumer - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [zD1JNWSqiGg](https://www.youtube.com/watch?v=zD1JNWSqiGg) | Daryl Hall &amp; Rumer - Take Me As I Am (Live From Daryl&#x27;s House) |
| 3 | 3 | [mcZ8edoG0OU](https://www.youtube.com/watch?v=mcZ8edoG0OU) | Daryl Hall &amp; Rumer - Be Thankful For What You Got (Live From Daryl&#x27;s House) |
| 4 | 4 | [rqZueHdXjb8](https://www.youtube.com/watch?v=rqZueHdXjb8) | Daryl Hall &amp; Rumer - Sara Smile (Live From Daryl&#x27;s House) |
| 5 | 5 | [zGYGXg1mBmk](https://www.youtube.com/watch?v=zGYGXg1mBmk) | Daryl Hall &amp; Rumer - Lady Day and John Coltrane (Live From Daryl&#x27;s House) |
| 6 | 6 | [9AT8rhBH-sw](https://www.youtube.com/watch?v=9AT8rhBH-sw) | Daryl Hall &amp; Rumer - Slow (Live From Daryl&#x27;s House) |
| 7 | 7 | [Rzr6mvDar30](https://www.youtube.com/watch?v=Rzr6mvDar30) | Daryl Hall &amp; Rumer - I Can&#x27;t Go For That (No Can Do) / End (Live From Daryl&#x27;s House) |

### E58: #58 - Daryl Hall hosts Nick Waterhouse on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtve9BIHu6qezOsN_64UNYcP9

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [8M9MdKi1flg](https://www.youtube.com/watch?v=8M9MdKi1flg) | Daryl Hall &amp; Nick Waterhouse - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [YR3VIZMjjt4](https://www.youtube.com/watch?v=YR3VIZMjjt4) | Daryl Hall &amp; Nick Waterhouse - Say I Wanna Know (Live From Daryl&#x27;s House) |
| 3 | 3 | [J6sT30TJ7DE](https://www.youtube.com/watch?v=J6sT30TJ7DE) | Daryl Hall &amp; Nick Waterhouse - Some Place (Live From Daryl&#x27;s House) |
| 4 | 4 | [lCnEQUx-cBk](https://www.youtube.com/watch?v=lCnEQUx-cBk) | Daryl Hall &amp; Nick Waterhouse - Problem With You (Live From Daryl&#x27;s House) |
| 5 | 5 | [t4nMeUM2mBM](https://www.youtube.com/watch?v=t4nMeUM2mBM) | Daryl Hall &amp; Nick Waterhouse - Time&#x27;s All Gone (Live From Daryl&#x27;s House) |
| 6 | 6 | [0o4a4vnzvc4](https://www.youtube.com/watch?v=0o4a4vnzvc4) | Daryl Hall &amp; Nick Waterhouse - If You Want Trouble (Live From Daryl&#x27;s House) |
| 7 | 7 | [po5s8h_zgt0](https://www.youtube.com/watch?v=po5s8h_zgt0) | Daryl Hall &amp; Nick Waterhouse - Hit The Road Jack (Live From Daryl&#x27;s House) |
| 8 | 8 | [U3XbTTlS89c](https://www.youtube.com/watch?v=U3XbTTlS89c) | Daryl Hall &amp; Nick Waterhouse - End (Live From Daryl&#x27;s House) |

### E59: #59 - Daryl Hall hosts Soul Revue on Live From Daryl&#x27;s House (Live at The Borgata)

https://www.youtube.com/playlist?list=PLINSQGXREtve2lAswaqi5WGGTiiHnZr9e

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [E30iEDwDxbY](https://www.youtube.com/watch?v=E30iEDwDxbY) | Daryl Hall with Sharon Jones and Allen Stone - Intro (Live at The Borgata) |
| 2 | 2 | [WP535ZNAe1I](https://www.youtube.com/watch?v=WP535ZNAe1I) | Daryl Hall with Sharon Jones and Allen Stone - Save Me (Live at The Borgata) |
| 3 | 3 | [ElP_3ZQchVQ](https://www.youtube.com/watch?v=ElP_3ZQchVQ) | Daryl Hall with Sharon Jones and Allen Stone - Eyes for You (Live at The Borgata) |
| 4 | 4 | [cRFQe93WJKw](https://www.youtube.com/watch?v=cRFQe93WJKw) | Daryl Hall with Sharon Jones and Allen Stone - Celebrate Tonight (Live at The Borgata) |
| 5 | 5 | [hEq-cTL3MFg](https://www.youtube.com/watch?v=hEq-cTL3MFg) | Daryl Hall with Sharon Jones and Allen Stone - Unaware (Live at The Borgata) |
| 6 | 6 | [TjEY_Yk_u5s](https://www.youtube.com/watch?v=TjEY_Yk_u5s) | Daryl Hall with Sharon Jones and Allen Stone - 100 Days, 100 Nights (Live at The Borgata) |
| 7 | 7 | [mGlo3BUA5Sg](https://www.youtube.com/watch?v=mGlo3BUA5Sg) | Daryl Hall with Sharon Jones and Allen Stone - I Learned The Hard Way (Live at The Borgata) |
| 8 | 8 | [h4qGH9EYcV8](https://www.youtube.com/watch?v=h4qGH9EYcV8) | Daryl Hall with Sharon Jones and Allen Stone - Everytime You Go Away (Live at The Borgata) |

### E60: #60 - Daryl Hall hosts Joe Walsh of The Eagles on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcibYqcUBQEqieNEOicj_Kq

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [O3mUsp6aspE](https://www.youtube.com/watch?v=O3mUsp6aspE) | Daryl Hall &amp; Joe Walsh - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [GPiz7vPEKPQ](https://www.youtube.com/watch?v=GPiz7vPEKPQ) | Daryl Hall &amp; Joe Walsh - Rocky Mountain Way (Live From Daryl&#x27;s House) |
| 3 | 3 | [eUvvpghxSb8](https://www.youtube.com/watch?v=eUvvpghxSb8) | Daryl Hall &amp; Joe Walsh - Life&#x27;s Been Good (Live From Daryl&#x27;s House) |
| 4 | 4 | [CEMqpFEyf2k](https://www.youtube.com/watch?v=CEMqpFEyf2k) | Daryl Hall &amp; Joe Walsh - Wrecking Ball (Live From Daryl&#x27;s House) |
| 5 | 5 | [S0Tmj6gkGi4](https://www.youtube.com/watch?v=S0Tmj6gkGi4) | Daryl Hall &amp; Joe Walsh - Someone Like You (Live From Daryl&#x27;s House) |
| 6 | 6 | [egUC_L_APLQ](https://www.youtube.com/watch?v=egUC_L_APLQ) | Daryl Hall &amp; Joe Walsh - Funk 49/50 (Live From Daryl&#x27;s House) |
| 7 | 7 | [JeO4KCbTHKQ](https://www.youtube.com/watch?v=JeO4KCbTHKQ) | Daryl Hall &amp; Joe Walsh (Eagles) - Wrong Side Of History (Live From Daryl&#x27;s House) |
| 8 | 8 | [9ZHqXY-k6F4](https://www.youtube.com/watch?v=9ZHqXY-k6F4) | Daryl Hall &amp; Joe Walsh - End (Live From Daryl&#x27;s House) |

### E61: #61 - Daryl Hall hosts Shelby Lynne on Live From Daryl&#x27;s House for Christmas

https://www.youtube.com/playlist?list=PLINSQGXREtvf96l9SWRj9J42IFuOMJ9bw

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [bBPdCP4ms0c](https://www.youtube.com/watch?v=bBPdCP4ms0c) | Daryl Hall &amp; Shelby Lynne - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [-lfr0CCPEJ8](https://www.youtube.com/watch?v=-lfr0CCPEJ8) | Daryl Hall &amp; Shelby Lynne - Ain&#x27;t Nothin&#x27; Like Christmas (Live From Daryl&#x27;s House) |
| 3 | 3 | [_gKd8dWw7FI](https://www.youtube.com/watch?v=_gKd8dWw7FI) | Daryl Hall &amp; Shelby Lynne - Leavin&#x27; (Live From Daryl&#x27;s House) |
| 4 | 4 | [3maJayWHons](https://www.youtube.com/watch?v=3maJayWHons) | Daryl Hall &amp; Shelby Lynne - Xmas (Live From Daryl&#x27;s House) |
| 5 | 5 | [78iSBEdcW4g](https://www.youtube.com/watch?v=78iSBEdcW4g) | Daryl Hall &amp; Shelby Lynne - Home For Christmas (Live From Daryl&#x27;s House) |
| 6 | 6 | [-MLKBI8HneM](https://www.youtube.com/watch?v=-MLKBI8HneM) | Daryl Hall &amp; Shelby Lynne - Bend (Live From Daryl&#x27;s House) |
| 7 | 7 | [wVQZGtbO_Uw](https://www.youtube.com/watch?v=wVQZGtbO_Uw) | Daryl Hall &amp; Shelby Lynne - Christmas Must Be Tonight (Live From Daryl&#x27;s House) |
| 8 | 8 | [zSJlfUS9UbY](https://www.youtube.com/watch?v=zSJlfUS9UbY) | Daryl Hall &amp; Shelby Lynne - End (Live From Daryl&#x27;s House) |

### E62: #62 - Daryl Hall hosts Minus The Bear on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfTgobdsq9Gf34CCp_rinTt

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [fFaagnxOFOw](https://www.youtube.com/watch?v=fFaagnxOFOw) | Daryl Hall &amp; Minus The Bear - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [WXP4u6lOtd8](https://www.youtube.com/watch?v=WXP4u6lOtd8) | Daryl Hall &amp; Minus The Bear - Into The Mirror (Live From Daryl&#x27;s House) |
| 3 | 3 | [oUVR-7UufkY](https://www.youtube.com/watch?v=oUVR-7UufkY) | Daryl Hall &amp; Minus The Bear - Listing (Live From Daryl&#x27;s House) |
| 4 | 4 | [liERAaXxlDY](https://www.youtube.com/watch?v=liERAaXxlDY) | Daryl Hall &amp; Minus The Bear - NYCNY (Live From Daryl&#x27;s House) |
| 5 | 5 | [5r2uJSS6odQ](https://www.youtube.com/watch?v=5r2uJSS6odQ) | Daryl Hall &amp; Minus The Bear - My Time (Live From Daryl&#x27;s House) |
| 6 | 6 | [07bnhpKpnkg](https://www.youtube.com/watch?v=07bnhpKpnkg) | Daryl Hall &amp; Minus The Bear - Steel and Blood (Live From Daryl&#x27;s House) |
| 7 | 7 | [QCmE99CZczA](https://www.youtube.com/watch?v=QCmE99CZczA) | Daryl Hall &amp; Minus The Bear - Get Out Of The Way (Live From Daryl&#x27;s House) |
| 8 | 8 | [572-aNzNSEo](https://www.youtube.com/watch?v=572-aNzNSEo) | Daryl Hall &amp; Minus The Bear - End (Live From Daryl&#x27;s House) |

### E63: #63 - Daryl Hall hosts Billy Gibbons of ZZ Top on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc7ZbsRTfXlnFda6isz7DEw

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [w13rRmDaEqw](https://www.youtube.com/watch?v=w13rRmDaEqw) | Daryl Hall &amp; Billy Gibbons - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [u685UUDtG2A](https://www.youtube.com/watch?v=u685UUDtG2A) | Daryl Hall &amp; Billy Gibbons - Thunderbird (Live From Daryl&#x27;s House) |
| 3 | 3 | [cx1vagukArE](https://www.youtube.com/watch?v=cx1vagukArE) | Daryl Hall &amp; Billy Gibbons - I Thank You (Live From Daryl&#x27;s House) |
| 4 | 4 | [iV3olvRoa7c](https://www.youtube.com/watch?v=iV3olvRoa7c) | Daryl Hall &amp; Billy Gibbons - Kiko (Live From Daryl&#x27;s House) |
| 5 | 5 | [W6LE8pFn1zw](https://www.youtube.com/watch?v=W6LE8pFn1zw) | Daryl Hall &amp; Billy Gibbons - Love You Like A Brother (Live From Daryl&#x27;s House) |
| 6 | 6 | [nzYPXxuCTHs](https://www.youtube.com/watch?v=nzYPXxuCTHs) | Daryl Hall &amp; Billy Gibbons - Sharp Dressed Man (Live From Daryl&#x27;s House) |
| 7 | 7 | [jKUbPoq2RKk](https://www.youtube.com/watch?v=jKUbPoq2RKk) | Daryl Hall &amp; Billy Gibbons (ZZ Top) - La Grange (Live From Daryl&#x27;s House) |
| 8 | 8 | [vJvJtoix3KU](https://www.youtube.com/watch?v=vJvJtoix3KU) | Daryl Hall &amp; Billy Gibbons - Bank On Your Love (Live From Daryl&#x27;s House) |
| 9 | 9 | [S-dWNxAN8SI](https://www.youtube.com/watch?v=S-dWNxAN8SI) | Daryl Hall &amp; Billy Gibbons - End (Live From Daryl&#x27;s House) |

### E64: #64 - Daryl Hall hosts Gavin DeGraw on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvegRkdfTBQwfw4P86Gu-E90

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [0iHobH3xO8Q](https://www.youtube.com/watch?v=0iHobH3xO8Q) | Daryl Hall &amp; Gavin DeGraw - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [J1IVrzBIjuo](https://www.youtube.com/watch?v=J1IVrzBIjuo) | Daryl Hall &amp; Gavin DeGraw - Make A Move (Live From Daryl&#x27;s House) |
| 3 | 3 | [M-8e2sYHOsM](https://www.youtube.com/watch?v=M-8e2sYHOsM) | Daryl Hall &amp; Gavin DeGraw - Go Solo (Live From Daryl&#x27;s House) |
| 4 | 4 | [drCyjPk4G4s](https://www.youtube.com/watch?v=drCyjPk4G4s) | Daryl Hall &amp; Gavin DeGraw - Everything Will Change (Live From Daryl&#x27;s House) |
| 5 | 5 | [CX_HJ0LuBRI](https://www.youtube.com/watch?v=CX_HJ0LuBRI) | Daryl Hall &amp; Gavin DeGraw - I Want To Know You For A Long Time (Live From Daryl&#x27;s House) |
| 6 | 6 | [fSeB7_5IFAs](https://www.youtube.com/watch?v=fSeB7_5IFAs) | Daryl Hall &amp; Gavin DeGraw - Radiation (Live From Daryl&#x27;s House) |
| 7 | 7 | [Yds-wAU7AQU](https://www.youtube.com/watch?v=Yds-wAU7AQU) | Daryl Hall &amp; Gavin DeGraw - I Don&#x27;t Wanna Be (Live From Daryl&#x27;s House) |

### E65: #65 - Daryl Hall hosts Johnnyswim on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdyuRWmLMSZnvzmJ1816LDs

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [mXa9mKIlE5c](https://www.youtube.com/watch?v=mXa9mKIlE5c) | Daryl Hall &amp; Johnnyswim - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [NEwCaYPuaaw](https://www.youtube.com/watch?v=NEwCaYPuaaw) | Daryl Hall &amp; Johnnyswim - Diamonds (Live From Daryl&#x27;s House) |
| 3 | 3 | [IzQzvunB6as](https://www.youtube.com/watch?v=IzQzvunB6as) | Daryl Hall &amp; Johnnyswim - Home (Live From Daryl&#x27;s House) |
| 4 | 4 | [Rq9nZ3VdFHw](https://www.youtube.com/watch?v=Rq9nZ3VdFHw) | Daryl Hall &amp; Johnnyswim - Adult Education (Live From Daryl&#x27;s House) |
| 5 | 5 | [zg4wo3RvBww](https://www.youtube.com/watch?v=zg4wo3RvBww) | Daryl Hall &amp; Johnnyswim - Heart Beats (Live From Daryl&#x27;s House) |
| 6 | 6 | [Jzfc89CFZnY](https://www.youtube.com/watch?v=Jzfc89CFZnY) | Daryl Hall &amp; Johnnyswim - Annie (Live From Daryl&#x27;s House) |
| 7 | 7 | [zt1Dgwdp538](https://www.youtube.com/watch?v=zt1Dgwdp538) | Daryl Hall &amp; Johnnyswim - Do What You Want, Be What You Are (Live From Daryl&#x27;s House) |
| 8 | 8 | [1CunK0wUdm4](https://www.youtube.com/watch?v=1CunK0wUdm4) | Daryl Hall &amp; Johnnyswim - End (Live From Daryl&#x27;s House) |

### E66: #66 - Daryl Hall hosts Amos Lee on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvfdTOPXPnxtxjnqFzZIHSnY

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [NqsfxyBuLL4](https://www.youtube.com/watch?v=NqsfxyBuLL4) | Daryl Hall &amp; Amos Lee - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [s86hoMAvyqI](https://www.youtube.com/watch?v=s86hoMAvyqI) | Daryl Hall &amp; Amos Lee - Windows Are Rolled Down (Live From Daryl&#x27;s House) |
| 3 | 3 | [WbWc0cgRzec](https://www.youtube.com/watch?v=WbWc0cgRzec) | Daryl Hall &amp; Amos Lee - Keep It Loose, Keep It Tight (Live From Daryl&#x27;s House) |
| 4 | 4 | [wzfNoxNTQeI](https://www.youtube.com/watch?v=wzfNoxNTQeI) | Daryl Hall &amp; Amos Lee - I&#x27;m In A Philly Mood (Live From Daryl&#x27;s House) |
| 5 | 5 | [w42mLMUw0so](https://www.youtube.com/watch?v=w42mLMUw0so) | Daryl Hall &amp; Amos Lee - Seen It All Before (Live From Daryl&#x27;s House) |
| 6 | 6 | [iFcXJoDu08w](https://www.youtube.com/watch?v=iFcXJoDu08w) | Daryl Hall &amp; Amos Lee - When The Morning Comes (Live From Daryl&#x27;s House) |
| 7 | 7 | [0z1y5aWE7Tk](https://www.youtube.com/watch?v=0z1y5aWE7Tk) | Daryl Hall &amp; Amos Lee - Method Of Modern Love (Live From Daryl&#x27;s House) |
| 8 | 8 | [OnZ58qtu8RE](https://www.youtube.com/watch?v=OnZ58qtu8RE) | Daryl Hall &amp; Amos Lee - Caramel ft. MUTLU (Live From Daryl&#x27;s House) |
| 9 | 9 | [M7Rj_dWyFg4](https://www.youtube.com/watch?v=M7Rj_dWyFg4) | Daryl Hall &amp; Amos Lee - End (Live From Daryl&#x27;s House) |

### E67: #67 - Daryl Hall hosts Brett Dennen on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdNa0zGRSsbCgrv3cNwD6Q2

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [Nc2KJyg7ekE](https://www.youtube.com/watch?v=Nc2KJyg7ekE) | Daryl Hall &amp; Brett Dennen - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [AH8w7rmlcTs](https://www.youtube.com/watch?v=AH8w7rmlcTs) | Daryl Hall &amp; Brett Dennen - Only Want You (Live From Daryl&#x27;s House) |
| 3 | 3 | [jQitaMaFfqw](https://www.youtube.com/watch?v=jQitaMaFfqw) | Daryl Hall &amp; Brett Dennen - Wild Child (Live From Daryl&#x27;s House) |
| 4 | 4 | [NfYO6JfDpUc](https://www.youtube.com/watch?v=NfYO6JfDpUc) | Daryl Hall &amp; Brett Dennen - Right as Rain (Live From Daryl&#x27;s House) |
| 5 | 5 | [s3b_B-JH-tY](https://www.youtube.com/watch?v=s3b_B-JH-tY) | Daryl Hall &amp; Brett Dennen - When We Were Young (Live From Daryl&#x27;s House) |
| 6 | 6 | [dIucukyZGZw](https://www.youtube.com/watch?v=dIucukyZGZw) | Daryl Hall &amp; Brett Dennen - What&#x27;s Gonna Happen To Us (Live From Daryl&#x27;s House) |
| 7 | 7 | [G4otrpomFvk](https://www.youtube.com/watch?v=G4otrpomFvk) | Daryl Hall &amp; Brett Dennen - Don&#x27;t Mess With Karma (Live From Daryl&#x27;s House) |
| 8 | 8 | [xQ53A9szopI](https://www.youtube.com/watch?v=xQ53A9szopI) | Daryl Hall &amp; Brett Dennen - End (Live From Daryl&#x27;s House) |

### E68: #68 - Daryl Hall hosts Darius Rucker of Hootie and The Blowfish on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvem3gWthZrEuRXHD0MhFsHL

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [0IoKTjwJpJ8](https://www.youtube.com/watch?v=0IoKTjwJpJ8) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [h0cjw3qGJxY](https://www.youtube.com/watch?v=h0cjw3qGJxY) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Alright (Live From Daryl&#x27;s House) |
| 3 | 3 | [vTqlrYia6g0](https://www.youtube.com/watch?v=vTqlrYia6g0) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Do It For Love (Live From Daryl&#x27;s House) |
| 4 | 4 | [UXie-gCrLlk](https://www.youtube.com/watch?v=UXie-gCrLlk) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Let Her Cry (Live From Daryl&#x27;s House) |
| 5 | 5 | [9TbStoACFww](https://www.youtube.com/watch?v=9TbStoACFww) | Daryl Hall &amp; Darius Rucker - You&#x27;ve Lost That Lovin&#x27; Feeling (Live From Daryl&#x27;s House) |
| 6 | 6 | [eiuu37HuoO0](https://www.youtube.com/watch?v=eiuu37HuoO0) | Daryl Hall &amp; Darius Rucker - Dinner Prep: Oyster Roast |
| 7 | 7 | [daeIlMD6_b8](https://www.youtube.com/watch?v=daeIlMD6_b8) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Laughing Down Crying (Live From Daryl&#x27;s House) |
| 8 | 8 | [d-mR2-cnuDU](https://www.youtube.com/watch?v=d-mR2-cnuDU) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - Wagon Wheel (Live From Daryl&#x27;s House) |
| 9 | 9 | [wwI_4jGk06E](https://www.youtube.com/watch?v=wwI_4jGk06E) | Daryl Hall &amp; Darius Rucker (Hootie &amp; the Blowfish) - End (Live From Daryl&#x27;s House) |

### E69: #69 - Daryl Hall hosts Sammy Hagar on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdhiQOPB9Zccn7zxa5Bp5ex

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [X_-jJHbho-k](https://www.youtube.com/watch?v=X_-jJHbho-k) | Daryl Hall &amp; Sammy Hagar - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [pbs0Ih7AA2U](https://www.youtube.com/watch?v=pbs0Ih7AA2U) | Daryl Hall &amp; Sammy Hagar - Rock Candy (Live From Daryl&#x27;s House) |
| 3 | 3 | [Uw7_jq3Uf0Y](https://www.youtube.com/watch?v=Uw7_jq3Uf0Y) | Daryl Hall &amp; Sammy Hagar - Family Man (Live From Daryl&#x27;s House) |
| 4 | 4 | [6mdPNmfJeTw](https://www.youtube.com/watch?v=6mdPNmfJeTw) | Daryl Hall &amp; Sammy Hagar - Your Love Is Driving Me Crazy (Live From Daryl&#x27;s House) |
| 5 | 5 | [qKKp487LnuE](https://www.youtube.com/watch?v=qKKp487LnuE) | Daryl Hall &amp; Sammy Hagar - Sexy Little Thing (Live From Daryl&#x27;s House) |
| 6 | 6 | [hWlo0SKnDD0](https://www.youtube.com/watch?v=hWlo0SKnDD0) | Daryl Hall &amp; Sammy Hagar - Foolish Pride (Live From Daryl&#x27;s House) |
| 7 | 7 | [HEdm-Xk6QmQ](https://www.youtube.com/watch?v=HEdm-Xk6QmQ) | Daryl Hall &amp; Sammy Hagar - I Can&#x27;t Drive 55 (Live From Daryl&#x27;s House) |
| 8 | 8 | [dCEEptZpfg4](https://www.youtube.com/watch?v=dCEEptZpfg4) | Daryl Hall &amp; Sammy Hagar - I&#x27;ll Fall In Love Again / End (Live From Daryl&#x27;s House) |

### E70: #70 - Daryl Hall hosts Ben Folds on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveWPM6DI4AutJ6Zptu_4EgQ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [mRgXrFKMwUw](https://www.youtube.com/watch?v=mRgXrFKMwUw) | Daryl Hall &amp; Ben Folds - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [X6D_Yv8g_Ig](https://www.youtube.com/watch?v=X6D_Yv8g_Ig) | Daryl Hall &amp; Ben Folds - Annie Waits (Live From Daryl&#x27;s House) |
| 3 | 3 | [cbBptMim5ZI](https://www.youtube.com/watch?v=cbBptMim5ZI) | Daryl Hall &amp; Ben Folds - Don&#x27;t Leave Me Alone With Her (Live From Daryl&#x27;s House) |
| 4 | 4 | [CUKC3iMkjBs](https://www.youtube.com/watch?v=CUKC3iMkjBs) | Daryl Hall &amp; Ben Folds - Landed (Live From Daryl&#x27;s House) |
| 5 | 5 | [ifCTs6M0bSE](https://www.youtube.com/watch?v=ifCTs6M0bSE) | Daryl Hall &amp; Ben Folds - Babs and Babs (Live From Daryl&#x27;s House) |
| 6 | 6 | [_s0Jn1q-kRc](https://www.youtube.com/watch?v=_s0Jn1q-kRc) | Daryl Hall &amp; Ben Folds - Private Eyes (Live From Daryl&#x27;s House) |
| 7 | 7 | [luVhKuvjDTw](https://www.youtube.com/watch?v=luVhKuvjDTw) | Daryl Hall &amp; Ben Folds - One Angry Dwarf and 200 Solemn Faces (Live From Daryl&#x27;s House) |
| 8 | 8 | [wIyeClQUGeE](https://www.youtube.com/watch?v=wIyeClQUGeE) | Daryl Hall &amp; Ben Folds - End (Live From Daryl&#x27;s House) |

### E71: #71 - Daryl Hall hosts Kandace Springs on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveY6b3LJkAQxPGYdRuGYA4P

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [xpA-mtL1JKU](https://www.youtube.com/watch?v=xpA-mtL1JKU) | Daryl Hall &amp; Kandace Springs - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [wMQ4oeVXLN0](https://www.youtube.com/watch?v=wMQ4oeVXLN0) | Daryl Hall &amp; Kandace Springs - Love Got In The Way (Live From Daryl&#x27;s House) |
| 3 | 3 | [_cP_UbHGeKw](https://www.youtube.com/watch?v=_cP_UbHGeKw) | Daryl Hall &amp; Kandace Springs - Everything Your Heart Desires (Live From Daryl&#x27;s House) |
| 4 | 4 | [3Gyxok2YazE](https://www.youtube.com/watch?v=3Gyxok2YazE) | Daryl Hall &amp; Kandace Springs - Teach Me (Live From Daryl&#x27;s House) |
| 5 | 5 | [tUo5VMLbmL8](https://www.youtube.com/watch?v=tUo5VMLbmL8) | Daryl Hall &amp; Kandace Springs - Meet Me In The Sky (Live From Daryl&#x27;s House) |
| 6 | 6 | [mmcANx0Ata8](https://www.youtube.com/watch?v=mmcANx0Ata8) | Daryl Hall &amp; Kandace Springs - Forbidden Fruit / August Day (Live From Daryl&#x27;s House) |
| 7 | 7 | [O19IPuVM3MM](https://www.youtube.com/watch?v=O19IPuVM3MM) | Daryl Hall &amp; Kandace Springs - End (Live From Daryl&#x27;s House) |

### E72: #72 - Daryl Hall hosts Aaron Neville on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvc_Qt4Lbo2-cfs4UuF1pLk5

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [3wWsX8pNEqk](https://www.youtube.com/watch?v=3wWsX8pNEqk) | Daryl Hall &amp; Aaron Neville - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [DilgbV2H32g](https://www.youtube.com/watch?v=DilgbV2H32g) | Daryl Hall &amp; Aaron Neville - Tell It Like It Is (Live From Daryl&#x27;s House) |
| 3 | 3 | [aXcySkQ5nN4](https://www.youtube.com/watch?v=aXcySkQ5nN4) | Daryl Hall &amp; Aaron Neville - Hercules (Live From Daryl&#x27;s House) |
| 4 | 4 | [CNcBDKYKOWs](https://www.youtube.com/watch?v=CNcBDKYKOWs) | Daryl Hall &amp; Aaron Neville - One On One (Live From Daryl&#x27;s House) |
| 5 | 5 | [zzme1U-nOls](https://www.youtube.com/watch?v=zzme1U-nOls) | Daryl Hall &amp; Aaron Neville - Can&#x27;t Stop My Heart From Loving You (The Rain Song) |
| 6 | 6 | [C4tVNOEoC8c](https://www.youtube.com/watch?v=C4tVNOEoC8c) | Daryl Hall &amp; Aaron Neville - It Feels Like Rain (Live From Daryl&#x27;s House) |
| 7 | 7 | [mZqvzLwHC3A](https://www.youtube.com/watch?v=mZqvzLwHC3A) | Daryl Hall &amp; Aaron Neville - All By Myself (Live From Daryl&#x27;s House) |
| 8 | 8 | [riL1AJU8Xgw](https://www.youtube.com/watch?v=riL1AJU8Xgw) | Daryl Hall &amp; Aaron Neville - Yellow Moon (Live From Daryl&#x27;s House) |
| 9 | 9 | [YaOm9zsmtC4](https://www.youtube.com/watch?v=YaOm9zsmtC4) | Daryl Hall &amp; Aaron Neville - End (Live From Daryl&#x27;s House) |

### E73: #73 - Daryl Hall hosts Kitty, Daisy &amp; Lewis on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvchL_s7exmAgmGTx_1S3B94

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-x5yTg7XMrk](https://www.youtube.com/watch?v=-x5yTg7XMrk) | Daryl Hall, Kitty, Daisy &amp; Lewis - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [yTEpt5fbAeE](https://www.youtube.com/watch?v=yTEpt5fbAeE) | Daryl Hall &amp; Kitty, Daisy &amp; Lewis - Baby Bye Bye (Live From Daryl&#x27;s House) |
| 3 | 3 | [hKV5_fBMWnI](https://www.youtube.com/watch?v=hKV5_fBMWnI) | Daryl Hall, Kitty, Daisy &amp; Lewis - Whenever You See Me (Live From Daryl&#x27;s House) |
| 4 | 4 | [RaacCiDWUrs](https://www.youtube.com/watch?v=RaacCiDWUrs) | Daryl Hall, Kitty, Daisy &amp; Lewis - No Action (Live From Daryl&#x27;s House) |
| 5 | 5 | [IT52c2OyCwU](https://www.youtube.com/watch?v=IT52c2OyCwU) | Daryl Hall, Kitty, Daisy &amp; Lewis - Feeling Of Wonder (Live From Daryl&#x27;s House) |
| 6 | 6 | [8xdv_cmzEgo](https://www.youtube.com/watch?v=8xdv_cmzEgo) | Daryl Hall, Kitty, Daisy &amp; Lewis - I&#x27;m Sorry (Live From Daryl&#x27;s House) |
| 7 | 7 | [9nlT8giqkBY](https://www.youtube.com/watch?v=9nlT8giqkBY) | Daryl Hall, Kitty, Daisy &amp; Lewis - Sacred Songs (Live From Daryl&#x27;s House) |
| 8 | 8 | [eFCVAooi9Kw](https://www.youtube.com/watch?v=eFCVAooi9Kw) | Daryl Hall, Kitty, Daisy &amp; Lewis - End (Live From Daryl&#x27;s House) |

### E74: #74 - Daryl Hall hosts Aloe Blacc on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvePXFMfab_DXTa46TnSPahk

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [4SAvhEGpozI](https://www.youtube.com/watch?v=4SAvhEGpozI) | Daryl Hall &amp; Aloe Blacc - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [FEa31sCcnn0](https://www.youtube.com/watch?v=FEa31sCcnn0) | Daryl Hall &amp; Aloe Blacc - I Need A Dollar (Live From Daryl&#x27;s House) |
| 3 | 3 | [r8GBLQ4Omyk](https://www.youtube.com/watch?v=r8GBLQ4Omyk) | Daryl Hall &amp; Aloe Blacc - Soul Violins (Live From Daryl&#x27;s House) |
| 4 | 4 | [egH0TyCd-pc](https://www.youtube.com/watch?v=egH0TyCd-pc) | Daryl Hall &amp; Aloe Blacc - I&#x27;m The Man (Live From Daryl&#x27;s House) |
| 5 | 5 | [2JoLkLuizNo](https://www.youtube.com/watch?v=2JoLkLuizNo) | Daryl Hall &amp; Aloe Blacc - Here Today (Live From Daryl&#x27;s House) |
| 6 | 6 | [WdTDJRO3WAg](https://www.youtube.com/watch?v=WdTDJRO3WAg) | Daryl Hall &amp; Aloe Blacc - What You See Is What You Get (Live From Daryl&#x27;s House) |
| 7 | 7 | [9TZV8M1lvoE](https://www.youtube.com/watch?v=9TZV8M1lvoE) | Daryl Hall &amp; Aloe Blacc - Wake Me Up (Live From Daryl&#x27;s House) |
| 8 | 8 | [pySUb_ul5wc](https://www.youtube.com/watch?v=pySUb_ul5wc) | Daryl Hall &amp; Aloe Blacc - Maneater / End (Live From Daryl&#x27;s House) |

### E75: #75 - Daryl Hall hosts Cheap Trick on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcKO-0JzfIAdmDM9lKm0tSZ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [r0zE3L1-uSE](https://www.youtube.com/watch?v=r0zE3L1-uSE) | Daryl Hall &amp; Cheap Trick - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [wiWHr__gl48](https://www.youtube.com/watch?v=wiWHr__gl48) | Daryl Hall &amp; Cheap Trick - Hello There / You Burn Me Up I&#x27;m A Cigarette (Live From Daryl&#x27;s House) |
| 3 | 3 | [nZPAiOhgTXA](https://www.youtube.com/watch?v=nZPAiOhgTXA) | Daryl Hall &amp; Cheap Trick - Family Man (Live From Daryl&#x27;s House) |
| 4 | 4 | [grx-UImsh7o](https://www.youtube.com/watch?v=grx-UImsh7o) | Daryl Hall &amp; Cheap Trick - Taxman, Mr. Thief (Live From Daryl&#x27;s House) |
| 5 | 5 | [PZdDqDmjD2Y](https://www.youtube.com/watch?v=PZdDqDmjD2Y) | Daryl Hall &amp; Cheap Trick - No Direction (Live From Daryl&#x27;s House) |
| 6 | 6 | [7vABJyeT8RE](https://www.youtube.com/watch?v=7vABJyeT8RE) | Daryl Hall &amp; Cheap Trick - Surrender (Live From Daryl&#x27;s House) |
| 7 | 7 | [BwG7yxQ9d5M](https://www.youtube.com/watch?v=BwG7yxQ9d5M) | Daryl Hall &amp; Cheap Trick - Heaven Tonight (Live From Daryl&#x27;s House) |
| 8 | 8 | [8QDyzT4b6To](https://www.youtube.com/watch?v=8QDyzT4b6To) | Daryl Hall &amp; Cheap Trick - I Want You To Want Me (Live From Daryl&#x27;s House) |
| 9 | 9 | [PJKUjLNjoLc](https://www.youtube.com/watch?v=PJKUjLNjoLc) | Daryl Hall &amp; Cheap Trick - End (Live From Daryl&#x27;s House) |

### E76: #76 - Daryl Hall hosts Wyclef Jean on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvf_rpjlCBU5ekWFlBgpuSrE

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [yOx92ABaXv4](https://www.youtube.com/watch?v=yOx92ABaXv4) | Daryl Hall &amp; Wyclef Jean (Fugees) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [5hOoO4RZaT8](https://www.youtube.com/watch?v=5hOoO4RZaT8) | Daryl Hall &amp; Wyclef Jean (Fugees) - Borrowed Time (Live From Daryl&#x27;s House) |
| 3 | 3 | [W5UbDCdl9Ps](https://www.youtube.com/watch?v=W5UbDCdl9Ps) | Daryl Hall &amp; Wyclef Jean (Fugees) - Gone Till November (Live From Daryl&#x27;s House) |
| 4 | 4 | [4hv-qoZsJ-M](https://www.youtube.com/watch?v=4hv-qoZsJ-M) | Daryl Hall &amp; Wyclef Jean (Fugees) - Ready or Not (Live From Daryl&#x27;s House) |
| 5 | 5 | [GDOdF5zogZM](https://www.youtube.com/watch?v=GDOdF5zogZM) | Daryl Hall &amp; Wyclef Jean (Fugees) - No Woman No Cry (Live From Daryl&#x27;s House) |
| 6 | 6 | [vBhotLjpg1A](https://www.youtube.com/watch?v=vBhotLjpg1A) | Daryl Hall &amp; Wyclef Jean (Fugees) - Wait For Me (Live From Daryl&#x27;s House) |
| 7 | 7 | [jw6GRLCNrjQ](https://www.youtube.com/watch?v=jw6GRLCNrjQ) | Daryl Hall &amp; Wyclef Jean (Fugees) - Rich Girl (Live From Daryl&#x27;s House) |
| 8 | 8 | [hMQB98fwS8A](https://www.youtube.com/watch?v=hMQB98fwS8A) | Daryl Hall &amp; Wyclef Jean (Fugees) - End (Live From Daryl&#x27;s House) |

### E77: #77 - Daryl Hall hosts Elle King on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvetcPedlyfTCBN6k6FaU3Wj

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [3zlwKS_bR_M](https://www.youtube.com/watch?v=3zlwKS_bR_M) | Daryl Hall &amp; Elle King - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [NJ44jOLYHUE](https://www.youtube.com/watch?v=NJ44jOLYHUE) | Daryl Hall &amp; Elle King - Ex&#x27;s and Oh&#x27;s (Live From Daryl&#x27;s House) |
| 3 | 3 | [99jHh4Y1ENQ](https://www.youtube.com/watch?v=99jHh4Y1ENQ) | Daryl Hall &amp; Elle King - Last Damn Night (Live From Daryl&#x27;s House) |
| 4 | 4 | [FxnZ_zGNIcQ](https://www.youtube.com/watch?v=FxnZ_zGNIcQ) | Daryl Hall &amp; Elle King - Under The Influence (Live From Daryl&#x27;s House) |
| 5 | 5 | [wDciyz_pa1w](https://www.youtube.com/watch?v=wDciyz_pa1w) | Daryl Hall &amp; Elle King - Good For Nothin&#x27; Woman (Live From Daryl&#x27;s House) |
| 6 | 6 | [_HHyjxLgo3w](https://www.youtube.com/watch?v=_HHyjxLgo3w) | Daryl Hall &amp; Elle King - Everytime You Go Away (Live From Daryl&#x27;s House) |
| 7 | 7 | [QWhsVTlD1b8](https://www.youtube.com/watch?v=QWhsVTlD1b8) | Daryl Hall &amp; Elle King - Say These Words Of Love (Live From Daryl&#x27;s House) |
| 8 | 8 | [6aXUYUXng1s](https://www.youtube.com/watch?v=6aXUYUXng1s) | Daryl Hall &amp; Elle King - End (Live From Daryl&#x27;s House) |

### E78: #78 - Daryl Hall hosts The O&#x27;Jays on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcy_DleHnvN4DGIK2cvMDpf

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [TDemadGFRVE](https://www.youtube.com/watch?v=TDemadGFRVE) | Daryl Hall &amp; The O&#x27;Jays - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [QYKyglyjtTw](https://www.youtube.com/watch?v=QYKyglyjtTw) | Daryl Hall &amp; The O&#x27;Jays - Love Train (Live From Daryl&#x27;s House) |
| 3 | 3 | [BRaB6Un2kAw](https://www.youtube.com/watch?v=BRaB6Un2kAw) | Daryl Hall &amp; The O&#x27;Jays - Back Stabbers (Live From Daryl&#x27;s House) |
| 4 | 4 | [Gm3jVkJ7IxE](https://www.youtube.com/watch?v=Gm3jVkJ7IxE) | Daryl Hall &amp; The O&#x27;Jays - I Love Music (Live From Daryl&#x27;s House) |
| 5 | 5 | [-Fn-slyzzNM](https://www.youtube.com/watch?v=-Fn-slyzzNM) | Daryl Hall &amp; The O&#x27;Jays - For The Love Of Money (Live From Daryl&#x27;s House) |
| 6 | 6 | [dhPBWFOZexc](https://www.youtube.com/watch?v=dhPBWFOZexc) | Daryl Hall &amp; The O&#x27;Jays - Use Ta Be My Girl (Live From Daryl&#x27;s House) |
| 7 | 7 | [itTVvNuhdyo](https://www.youtube.com/watch?v=itTVvNuhdyo) | Daryl Hall &amp; The O&#x27;Jays - I Want To Know You For A Long Time (Live From Daryl&#x27;s House) |
| 8 | 8 | [ncyj7zrNggM](https://www.youtube.com/watch?v=ncyj7zrNggM) | Daryl Hall &amp; The O&#x27;Jays - I Can&#x27;t Go For That (No Can Do) (Live From Daryl&#x27;s House) |
| 9 | 9 | [LNDL8xSaLus](https://www.youtube.com/watch?v=LNDL8xSaLus) | Daryl Hall &amp; The O&#x27;Jays - End (Live From Daryl&#x27;s House) |

### E79: #79 - Daryl Hall hosts Anderson East on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvd73SQQrFNyZkGqNiIxL_7f

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [WLbKQLL3Zn4](https://www.youtube.com/watch?v=WLbKQLL3Zn4) | Daryl Hall &amp; Anderson East - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [do4gRMgUOsw](https://www.youtube.com/watch?v=do4gRMgUOsw) | Daryl Hall &amp; Anderson East - Devil In Me (Live From Daryl&#x27;s House) |
| 3 | 3 | [WuiQWipoB3U](https://www.youtube.com/watch?v=WuiQWipoB3U) | Daryl Hall &amp; Anderson East - Only You (Live From Daryl&#x27;s House) |
| 4 | 4 | [1t_6aki-gfI](https://www.youtube.com/watch?v=1t_6aki-gfI) | Daryl Hall &amp; Anderson East - Find &#x27;Em, Fool &#x27;Em and Forget &#x27;Em (Live From Daryl&#x27;s House) |
| 5 | 5 | [rSy2Z275xmY](https://www.youtube.com/watch?v=rSy2Z275xmY) | Daryl Hall &amp; Anderson East - Learning (Live From Daryl&#x27;s House) |
| 6 | 6 | [jOGCy5rXcWg](https://www.youtube.com/watch?v=jOGCy5rXcWg) | Daryl Hall &amp; Anderson East - Satisfy Me (Live From Daryl&#x27;s House) |
| 7 | 7 | [rFxvXYs9g4E](https://www.youtube.com/watch?v=rFxvXYs9g4E) | Daryl Hall &amp; Anderson East - Guessing Games (Live From Daryl&#x27;s House) |
| 8 | 8 | [K1hCGR6OwOQ](https://www.youtube.com/watch?v=K1hCGR6OwOQ) | Daryl Hall &amp; Anderson East - She&#x27;s Gone (Live From Daryl&#x27;s House) |
| 9 | 9 | [JuWBGffGfpE](https://www.youtube.com/watch?v=JuWBGffGfpE) | Daryl Hall &amp; Anderson East - End (Live From Daryl&#x27;s House) |

### E80: #80 - Daryl Hall hosts Daughtry on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcv_xxFSjjOAfqCDSqZfNjq

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [-O0yfpjbLcs](https://www.youtube.com/watch?v=-O0yfpjbLcs) | Daryl Hall &amp; Daughtry - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [0wTe-gsvyu4](https://www.youtube.com/watch?v=0wTe-gsvyu4) | Daryl Hall &amp; Daughtry - Home (Live From Daryl&#x27;s House) |
| 3 | 3 | [U3-JgpAfwjM](https://www.youtube.com/watch?v=U3-JgpAfwjM) | Daryl Hall &amp; Daughtry - September (Live From Daryl&#x27;s House) |
| 4 | 4 | [hCEXOPUfVoc](https://www.youtube.com/watch?v=hCEXOPUfVoc) | Daryl Hall &amp; Daughtry - It&#x27;s Not Over (Live From Daryl&#x27;s House) |
| 5 | 5 | [g-cFRm0NiwM](https://www.youtube.com/watch?v=g-cFRm0NiwM) | Daryl Hall &amp; Daughtry - Torches (Live From Daryl&#x27;s House) |
| 6 | 6 | [awYafGdeT_Q](https://www.youtube.com/watch?v=awYafGdeT_Q) | Daryl Hall &amp; Daughtry - Waiting For Superman (Live From Daryl&#x27;s House) |
| 7 | 7 | [J_aLMFV7BDE](https://www.youtube.com/watch?v=J_aLMFV7BDE) | Daryl Hall &amp; Daughtry - Out Of Touch (Live From Daryl&#x27;s House) |
| 8 | 8 | [AhrXVilqII0](https://www.youtube.com/watch?v=AhrXVilqII0) | Daryl Hall &amp; Daughtry - So Close (Live From Daryl&#x27;s House) |
| 9 | 9 | [58_RgKsPpHw](https://www.youtube.com/watch?v=58_RgKsPpHw) | Daryl Hall &amp; Daughtry - End (Live From Daryl&#x27;s House) |

### E81: #81 - Daryl Hall hosts SayGrace on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcbqtO9AMAp9yAqagSIRBYv

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [sykS4St4EzY](https://www.youtube.com/watch?v=sykS4St4EzY) | Daryl Hall &amp; SayGrace - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [qZ86H99Iq4c](https://www.youtube.com/watch?v=qZ86H99Iq4c) | Daryl Hall &amp; SayGrace - Hell of a Girl (Live From Daryl&#x27;s House) |
| 3 | 3 | [4vCwYjVf3Q0](https://www.youtube.com/watch?v=4vCwYjVf3Q0) | Daryl Hall &amp; SayGrace - You Don&#x27;t Own Me (Live From Daryl&#x27;s House) |
| 4 | 4 | [9qDugcppdZI](https://www.youtube.com/watch?v=9qDugcppdZI) | Daryl Hall &amp; SayGrace - Why Do Lovers Break Each Other&#x27;s Heart? (Live From Daryl&#x27;s House) |
| 5 | 5 | [wh0JAn0_3LQ](https://www.youtube.com/watch?v=wh0JAn0_3LQ) | Daryl Hall &amp; SayGrace - Boyfriend Jeans (Live From Daryl&#x27;s House) |
| 6 | 6 | [lIvt_TxiFzo](https://www.youtube.com/watch?v=lIvt_TxiFzo) | Daryl Hall &amp; SayGrace - How To Love Me (Live From Daryl&#x27;s House) |
| 7 | 7 | [_pjZGrfgIY0](https://www.youtube.com/watch?v=_pjZGrfgIY0) | Daryl Hall &amp; SayGrace - Your Imagination (Live From Daryl&#x27;s House) |
| 8 | 8 | [LUb5LdmFQWs](https://www.youtube.com/watch?v=LUb5LdmFQWs) | Daryl Hall &amp; SayGrace - End (Live From Daryl&#x27;s House) |

### E82: #82 - Daryl Hall hosts Kenny Loggins on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvd8drXYA7JUwQP9vMywQFYo

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [0QsnCCS0s1c](https://www.youtube.com/watch?v=0QsnCCS0s1c) | Daryl Hall &amp; Kenny Loggins - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [v0YNyHcwIcA](https://www.youtube.com/watch?v=v0YNyHcwIcA) | Daryl Hall &amp; Kenny Loggins - Your Mama Don&#x27;t Dance (Live From Daryl&#x27;s House) |
| 3 | 3 | [ybsZIsOqTSo](https://www.youtube.com/watch?v=ybsZIsOqTSo) | Daryl Hall &amp; Kenny Loggins - Footloose (Live From Daryl&#x27;s House) |
| 4 | 4 | [8lk3MEl4BHM](https://www.youtube.com/watch?v=8lk3MEl4BHM) | Daryl Hall &amp; Kenny Loggins - I&#x27;m Alright (Live From Daryl&#x27;s House) |
| 5 | 5 | [uyRC9l-SzsA](https://www.youtube.com/watch?v=uyRC9l-SzsA) | Daryl Hall &amp; Kenny Loggins - It&#x27;s Uncanny (Live From Daryl&#x27;s House) |
| 6 | 6 | [qVWPLfK2JHU](https://www.youtube.com/watch?v=qVWPLfK2JHU) | Daryl Hall &amp; Kenny Loggins - Danny&#x27;s Song (Live From Daryl&#x27;s House) |
| 7 | 7 | [H1JL12xC8kk](https://www.youtube.com/watch?v=H1JL12xC8kk) | Daryl Hall &amp; Kenny Loggins - This Is It (Live From Daryl&#x27;s House) |
| 8 | 8 | [83DcFBshXNg](https://www.youtube.com/watch?v=83DcFBshXNg) | Daryl Hall &amp; Kenny Loggins - You Make My Dreams (Live From Daryl&#x27;s House) |
| 9 | 9 | [f0yyiWkuOao](https://www.youtube.com/watch?v=f0yyiWkuOao) | Daryl Hall &amp; Kenny Loggins - End (Live From Daryl&#x27;s House) |

### E83: #83 - Daryl Hall hosts Tommy Shaw of Styx on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcPFDvw_vLiZo5YXDscmflu

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [8iu7IJPV2vY](https://www.youtube.com/watch?v=8iu7IJPV2vY) | Daryl Hall &amp; Tommy Shaw (Styx) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [mlLx41y4pxg](https://www.youtube.com/watch?v=mlLx41y4pxg) | Daryl Hall &amp; Tommy Shaw (Styx) - Blue Collar Man (Live From Daryl&#x27;s House) |
| 3 | 3 | [cikuFFJjR64](https://www.youtube.com/watch?v=cikuFFJjR64) | Daryl Hall &amp; Tommy Shaw (Styx) - Renegade (Live From Daryl&#x27;s House) |
| 4 | 4 | [n99bKXKQvag](https://www.youtube.com/watch?v=n99bKXKQvag) | Daryl Hall &amp; Tommy Shaw (Styx) - Too Much Time On My Hands (Live From Daryl&#x27;s House) |
| 5 | 5 | [LpWEHvM74OY](https://www.youtube.com/watch?v=LpWEHvM74OY) | Daryl Hall &amp; Tommy Shaw (Styx) - Searching For My Love (Live From Daryl&#x27;s House) |
| 6 | 6 | [l6PV9VeG_fc](https://www.youtube.com/watch?v=l6PV9VeG_fc) | Daryl Hall &amp; Tommy Shaw (Styx) - It&#x27;s A Laugh (Live From Daryl&#x27;s House) |
| 7 | 7 | [iMLohbnBZ1o](https://www.youtube.com/watch?v=iMLohbnBZ1o) | Daryl Hall &amp; Tommy Shaw (Styx) - Delayed Reaction (Live From Daryl&#x27;s House) |
| 8 | 8 | [QXejzNn7TVU](https://www.youtube.com/watch?v=QXejzNn7TVU) | Daryl Hall &amp; Tommy Shaw (Styx) - End (Live From Daryl&#x27;s House) |

### E84: #84 - Daryl Hall hosts Ty Taylor of Vintage Trouble on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdhHIzkScMCGgC6hAimjHTG

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [j7hPdE8iRr8](https://www.youtube.com/watch?v=j7hPdE8iRr8) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [_oRV4PD7URI](https://www.youtube.com/watch?v=_oRV4PD7URI) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Nobody Told Me (Live From Daryl&#x27;s House) |
| 3 | 3 | [1V7KsLcEtXQ](https://www.youtube.com/watch?v=1V7KsLcEtXQ) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Another Man&#x27;s Words (Live From Daryl&#x27;s House) |
| 4 | 4 | [qtQYWzbS5MA](https://www.youtube.com/watch?v=qtQYWzbS5MA) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Can&#x27;t Stop Rollin&#x27; (Live From Daryl&#x27;s House) |
| 5 | 5 | [lbXqDhbH5us](https://www.youtube.com/watch?v=lbXqDhbH5us) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Do Me Right (Live From Daryl&#x27;s House) |
| 6 | 6 | [9BFD6gaPHIY](https://www.youtube.com/watch?v=9BFD6gaPHIY) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - Fools Rush In (Live From Daryl&#x27;s House) |
| 7 | 7 | [tOSaBROsp_s](https://www.youtube.com/watch?v=tOSaBROsp_s) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - I&#x27;ll Be Around (Live From Daryl&#x27;s House) |
| 8 | 8 | [8zSdY0s3K6Y](https://www.youtube.com/watch?v=8zSdY0s3K6Y) | Daryl Hall &amp; Ty Taylor (Vintage Trouble) - End (Live From Daryl&#x27;s House) |

### E85: #85 - Daryl Hall hosts Glenn Tilbrook of Squeeze on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvczpZBPRlWqSPMKSOvmX1Er

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [ROSh-yfjGKQ](https://www.youtube.com/watch?v=ROSh-yfjGKQ) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [E4uy-2RTdXw](https://www.youtube.com/watch?v=E4uy-2RTdXw) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Black Coffee In Bed (Live From Daryl&#x27;s House) |
| 3 | 3 | [6F1P2PzKkcY](https://www.youtube.com/watch?v=6F1P2PzKkcY) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Hourglass (Live From Daryl&#x27;s House) |
| 4 | 4 | [g4vuq9eV2K0](https://www.youtube.com/watch?v=g4vuq9eV2K0) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Pulling Mussels From The Shell (Live From Daryl&#x27;s House) |
| 5 | 5 | [wV09rq5CzDw](https://www.youtube.com/watch?v=wV09rq5CzDw) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Tempted (Live From Daryl&#x27;s House) |
| 6 | 6 | [QvaB4-1uCRs](https://www.youtube.com/watch?v=QvaB4-1uCRs) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Romeo Is Bleeding (Live From Daryl&#x27;s House) |
| 7 | 7 | [hQ9veDReeZA](https://www.youtube.com/watch?v=hQ9veDReeZA) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - Throw The Roses Away (Live From Daryl&#x27;s House) |
| 8 | 8 | [mz_N6vf8pLU](https://www.youtube.com/watch?v=mz_N6vf8pLU) | Daryl Hall &amp; Glenn Tilbrook (Squeeze) - End (Live From Daryl&#x27;s House) |

### E86: #86 - Daryl Hall hosts Charlie Starr of Blackberry Smoke on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcV3Q26wTKxcpzrLnfjNQ4v

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [MWXuF2TOKOk](https://www.youtube.com/watch?v=MWXuF2TOKOk) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [dGQUIW0b2BI](https://www.youtube.com/watch?v=dGQUIW0b2BI) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Waiting For The Thunder (Live From Daryl&#x27;s House) |
| 3 | 3 | [QJ4SN6I0V2k](https://www.youtube.com/watch?v=QJ4SN6I0V2k) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - One Horse Town (Live From Daryl&#x27;s House) |
| 4 | 4 | [XyN9MF-N480](https://www.youtube.com/watch?v=XyN9MF-N480) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Run Away From It All (Live From Daryl&#x27;s House) |
| 5 | 5 | [GnEjsdr3ycs](https://www.youtube.com/watch?v=GnEjsdr3ycs) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Ain&#x27;t Much Left Of Me (Live From Daryl&#x27;s House) |
| 6 | 6 | [FZvBXAODM6k](https://www.youtube.com/watch?v=FZvBXAODM6k) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Message To Ya (Live From Daryl&#x27;s House) |
| 7 | 7 | [QyLp8GonnnM](https://www.youtube.com/watch?v=QyLp8GonnnM) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - Survive (Live From Daryl&#x27;s House) |
| 8 | 8 | [z8U7d_dyDFc](https://www.youtube.com/watch?v=z8U7d_dyDFc) | Daryl Hall &amp; Charlie Starr (Blackberry Smoke) - End (Live From Daryl&#x27;s House) |

### E87: #87 - Daryl Hall hosts Robert Fripp on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdnvCfLXTt0GmE8Oz_8s2tQ

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [rVo_cDe3uy4](https://www.youtube.com/watch?v=rVo_cDe3uy4) | Daryl Hall &amp; Robert Fripp (King Crimson) - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [cHs2S51OSh8](https://www.youtube.com/watch?v=cHs2S51OSh8) | Daryl Hall &amp; Robert Fripp (King Crimson) - You Burn Me Up I&#x27;m A Cigarette (Live From Daryl&#x27;s House) |
| 3 | 3 | [xd7BdzzY8BQ](https://www.youtube.com/watch?v=xd7BdzzY8BQ) | Daryl Hall &amp; Robert Fripp (King Crimson) - NYCNY (Live From Daryl&#x27;s House) |
| 4 | 4 | [Qbe2_TYliTo](https://www.youtube.com/watch?v=Qbe2_TYliTo) | Daryl Hall &amp; Robert Fripp (King Crimson) - Heroes (Live From Daryl&#x27;s House) |
| 5 | 5 | [6PAHYXc3gcw](https://www.youtube.com/watch?v=6PAHYXc3gcw) | Daryl Hall &amp; Robert Fripp (King Crimson) - Babs and Babs (Live From Daryl&#x27;s House) |
| 6 | 6 | [kkb783rNjO0](https://www.youtube.com/watch?v=kkb783rNjO0) | Daryl Hall &amp; Robert Fripp (King Crimson) - Red (Live From Daryl&#x27;s House) |
| 7 | 7 | [OJ70W7XUCSU](https://www.youtube.com/watch?v=OJ70W7XUCSU) | Daryl Hall &amp; Robert Fripp (King Crimson) - The Farther Away I Am (Live From Daryl&#x27;s House) |
| 8 | 8 | [RwxAgtJzJI4](https://www.youtube.com/watch?v=RwxAgtJzJI4) | Daryl Hall &amp; Robert Fripp (King Crimson) - End (Live From Daryl&#x27;s House) |

### E88: #88 - Daryl Hall hosts Andy Grammer on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtveW4HQ3qocWr6AEk6xGb7Vv

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [F69y2WRgxbk](https://www.youtube.com/watch?v=F69y2WRgxbk) | Daryl Hall &amp; Andy Grammer - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [DfKDQQBYIqo](https://www.youtube.com/watch?v=DfKDQQBYIqo) | Daryl Hall &amp; Andy Grammer - Keep Your Head Up (Live From Daryl&#x27;s House) |
| 3 | 3 | [6MSMjHIjTw4](https://www.youtube.com/watch?v=6MSMjHIjTw4) | Daryl Hall &amp; Andy Grammer - Honey, I&#x27;m Good (Live From Daryl&#x27;s House) |
| 4 | 4 | [Ygmrh5POwAQ](https://www.youtube.com/watch?v=Ygmrh5POwAQ) | Daryl Hall &amp; Andy Grammer - Love Is The New Money (Live From Daryl&#x27;s House) |
| 5 | 5 | [GAcoNfF9C3E](https://www.youtube.com/watch?v=GAcoNfF9C3E) | Daryl Hall &amp; Andy Grammer - Soul Violins (Live From Daryl&#x27;s House) |
| 6 | 6 | [pq6rsytIt_o](https://www.youtube.com/watch?v=pq6rsytIt_o) | Daryl Hall &amp; Andy Grammer - Starting All Over Again (Live From Daryl&#x27;s House) |
| 7 | 7 | [4plCqoCqEaY](https://www.youtube.com/watch?v=4plCqoCqEaY) | Daryl Hall &amp; Andy Grammer - Fresh Eyes (Live From Daryl&#x27;s House) |
| 8 | 8 | [pOZ3NBVJRCE](https://www.youtube.com/watch?v=pOZ3NBVJRCE) | Daryl Hall &amp; Andy Grammer - End (Live From Daryl&#x27;s House) |

### E89: #89 - Daryl Hall hosts Lisa Loeb on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcAkWGPYI_jmuRpFpXK5-wc

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [K8OhGfCsldw](https://www.youtube.com/watch?v=K8OhGfCsldw) | Daryl Hall &amp; Lisa Loeb - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [QiXPYwg9Xgk](https://www.youtube.com/watch?v=QiXPYwg9Xgk) | Daryl Hall &amp; Lisa Loeb - Another Day (Live From Daryl&#x27;s House) |
| 3 | 3 | [stB8G8bT4uQ](https://www.youtube.com/watch?v=stB8G8bT4uQ) | Daryl Hall &amp; Lisa Loeb - Stay (Live From Daryl&#x27;s House) |
| 4 | 4 | [26dx2KgVZDY](https://www.youtube.com/watch?v=26dx2KgVZDY) | Daryl Hall &amp; Lisa Loeb - O-O-H Child (Live From Daryl&#x27;s House) |
| 5 | 5 | [EDMQBsNGhfk](https://www.youtube.com/watch?v=EDMQBsNGhfk) | Daryl Hall &amp; Lisa Loeb - Rich Girl (Live From Daryl&#x27;s House) |
| 6 | 6 | [VJKXSesM3Is](https://www.youtube.com/watch?v=VJKXSesM3Is) | Daryl Hall &amp; Lisa Loeb - This Is My Life (Live From Daryl&#x27;s House) |
| 7 | 7 | [-i5I6CerUas](https://www.youtube.com/watch?v=-i5I6CerUas) | Daryl Hall &amp; Lisa Loeb - I Do (Live From Daryl&#x27;s House) |
| 8 | 8 | [SbfPwTe_MZI](https://www.youtube.com/watch?v=SbfPwTe_MZI) | Daryl Hall &amp; Lisa Loeb - End (Live From Daryl&#x27;s House) |

### E90: #90 - Daryl Hall hosts Howard Jones on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvdQSlQ8xUqyOrdl7mRPUdOE

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [GrFOQpd0OU8](https://www.youtube.com/watch?v=GrFOQpd0OU8) | Daryl Hall &amp; Howard Jones - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [tQtL5GjjEb0](https://www.youtube.com/watch?v=tQtL5GjjEb0) | Daryl Hall &amp; Howard Jones - What Is Love (Live From Daryl&#x27;s House) |
| 3 | 3 | [GzxMf1T4Y2Q](https://www.youtube.com/watch?v=GzxMf1T4Y2Q) | Daryl Hall &amp; Howard Jones - Things Can Only Get Better (Live From Daryl&#x27;s House) |
| 4 | 4 | [bWbMM_7yiAM](https://www.youtube.com/watch?v=bWbMM_7yiAM) | Daryl Hall &amp; Howard Jones - No One Is To Blame (Live From Daryl&#x27;s House) |
| 5 | 5 | [_Mgt7pnEIwQ](https://www.youtube.com/watch?v=_Mgt7pnEIwQ) | Daryl Hall &amp; Howard Jones - Like To Get To Know You Well (Live From Daryl&#x27;s House) |
| 6 | 6 | [I4XCGrhpXLw](https://www.youtube.com/watch?v=I4XCGrhpXLw) | Daryl Hall &amp; Howard Jones - Let Love Take Control (Live From Daryl&#x27;s House) |
| 7 | 7 | [YyW6L9h2sbw](https://www.youtube.com/watch?v=YyW6L9h2sbw) | Daryl Hall &amp; Howard Jones - I&#x27;m In A Philly Mood (Live From Daryl&#x27;s House) |
| 8 | 8 | [STn0JtvgwIo](https://www.youtube.com/watch?v=STn0JtvgwIo) | Daryl Hall &amp; Howard Jones - End (Live From Daryl&#x27;s House) |

### E91: #91 - Daryl Hall hosts Dave Stewart &amp; Vanessa Amorosi on Live From Daryl&#x27;s House

https://www.youtube.com/playlist?list=PLINSQGXREtvcwnOwZyKjjpVRw3FDYEYCe

| Position | Playlist index | Video ID | Clip title |
|---:|---:|---|---|
| 1 | 1 | [RvK0AAq3rlA](https://www.youtube.com/watch?v=RvK0AAq3rlA) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Intro (Live From Daryl&#x27;s House) |
| 2 | 2 | [e-EVVNktIPw](https://www.youtube.com/watch?v=e-EVVNktIPw) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - How Long (Live From Daryl&#x27;s House) |
| 3 | 3 | [gloB11zfHUI](https://www.youtube.com/watch?v=gloB11zfHUI) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Too Much Of A Heartache (Live From Daryl&#x27;s House) |
| 4 | 4 | [wI-BllMnNKI](https://www.youtube.com/watch?v=wI-BllMnNKI) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - The Whole World&#x27;s Better (Live From Daryl&#x27;s House) |
| 5 | 5 | [YR6WpubzJsI](https://www.youtube.com/watch?v=YR6WpubzJsI) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Can&#x27;t Say No To You (Live From Daryl&#x27;s House) |
| 6 | 6 | [2hmk-oN1xO8](https://www.youtube.com/watch?v=2hmk-oN1xO8) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Walking In Between Raindrops (Live From Daryl&#x27;s House) |
| 7 | 7 | [wCKaj9sOuN4](https://www.youtube.com/watch?v=wCKaj9sOuN4) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Too Much Information (Live From Daryl&#x27;s House) |
| 8 | 8 | [on8ZRW168OU](https://www.youtube.com/watch?v=on8ZRW168OU) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Ball and Chain (Live From Daryl&#x27;s House) |
| 9 | 9 | [Qg_dBHY8_54](https://www.youtube.com/watch?v=Qg_dBHY8_54) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - Rather Be A Fool (Live From Daryl&#x27;s House) |
| 10 | 10 | [fICr1gvCwnA](https://www.youtube.com/watch?v=fICr1gvCwnA) | Daryl Hall, Dave Stewart &amp; Vanessa Amorosi - End (Live From Daryl&#x27;s House) |

