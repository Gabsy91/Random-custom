# Graph Report - Random-custom  (2026-11-20)

## Corpus Check
- 346 files · ~305,341 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 7, .woff2 6)

## Summary
- 1146 nodes · 2417 edges · 96 communities (66 shown, 30 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 97 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95

## God Nodes (most connected - your core abstractions)
1. `IndicatorResult` - 57 edges
2. `IndicatorConfig` - 52 edges
3. `BaseIndicator` - 38 edges
4. `TechnicalUtils` - 32 edges
5. `IndicatorCategory` - 28 edges
6. `register_indicator()` - 26 edges
7. `IndicatorManager` - 17 edges
8. `resolveSfx()` - 14 edges
9. `compileCutList()` - 14 edges
10. `freezeRecipe()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `run()` --calls--> `main()`  [EXTRACTED]
  .agents/skills/media-use/audio/scripts/heygen-voice.test.mjs → .agents/skills/media-use/audio/scripts/heygen-voice.mjs
- `ATR` --uses--> `IndicatorCategory`  [INFERRED]
  .agents/skills/technical-analysis/src/kline_indicators.py → .agents/skills/technical-analysis/src/kline_indicator_utils.py
- `AVL` --uses--> `IndicatorCategory`  [INFERRED]
  .agents/skills/technical-analysis/src/kline_indicators.py → .agents/skills/technical-analysis/src/kline_indicator_utils.py
- `BOLL` --uses--> `IndicatorCategory`  [INFERRED]
  .agents/skills/technical-analysis/src/kline_indicators.py → .agents/skills/technical-analysis/src/kline_indicator_utils.py
- `CCI` --uses--> `IndicatorCategory`  [INFERRED]
  .agents/skills/technical-analysis/src/kline_indicators.py → .agents/skills/technical-analysis/src/kline_indicator_utils.py

## Import Cycles
- None detected.

## Communities (96 total, 30 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (56): withFileLock(), globalMediaDir(), mediaHome(), dedupe(), emptyFile(), isRecord(), mergedPreferences(), PREFERENCE_KEYS (+48 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (17): CLI_MEDIA_USE, SKILLS, skillScripts(), script, run(), savedEnv, openAudioMeta(), AUDIO (+9 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (41): escapeRegExp(), readTargetAttrs(), run(), { values: args }, bareToken(), clampRanges(), cleanRange(), compileCutList() (+33 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (35): recordInManifest(), SFX_SOURCES, noBgm, voicePaths(), writtenAssets(), record(), formatDims(), formatDur() (+27 more)

### Community 4 - "Community 4"
Cohesion: 0.12
Nodes (23): agentWritePath(), httpsUrl(), oneLine(), OPENVERSE_SFX_LICENSES, OpenverseUnavailableError, penalty(), pickOpenverseSfx(), PLAYABLE_FILETYPES (+15 more)

### Community 5 - "Community 5"
Cohesion: 0.09
Nodes (26): countAssetFiles(), walk(), escapeHtml(), evalBlock(), generateReport(), outPath, REPO_ROOT, report (+18 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (3): DataValidator, get_registered_indicators(), IndicatorManager

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (23): anomalies, argv, audioMeta, bgmFields, bgmModeOverride, HERE, hyperframesDir, langOverride (+15 more)

### Community 8 - "Community 8"
Cohesion: 0.13
Nodes (23): billingRefusal(), envFileText(), errorCode(), HEYGEN_BASE, HEYGEN_CLI_SOURCE_HEADERS, HEYGEN_CLIENT_SOURCE_HEADERS, heygenAuthMethod(), heygenBase() (+15 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (4): FIB, MA, ROC, VOL

### Community 11 - "Community 11"
Cohesion: 0.18
Nodes (17): attrOf(), carveSources(), decode(), DEFAULT_STRENGTH, detectTracks(), escapeAttr(), fail(), groupSourceRefusal() (+9 more)

### Community 12 - "Community 12"
Cohesion: 0.16
Nodes (18): ffmpegDurationFallback(), ffprobeDuration(), launchingCliCommand(), MISSING_CLI_MESSAGE, parseFfmpegDurationBanner(), relTo(), _resetNpxResolutionWarnForTests(), resolveNpxCliFromNpmExecPath() (+10 more)

### Community 13 - "Community 13"
Cohesion: 0.09
Nodes (10): CENTER, COUNTRIES, framesDir, MARGIN, N, [cmd, ...rest], font(), gridFilters() (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.18
Nodes (19): frameRateNumber(), IMAGE_EXTENSIONS, OUTPUT_IMAGE_EXTENSIONS, probe(), processImage(), processVideo(), run(), temporaryOutput() (+11 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (7): _find_matching_paren(), Finding, lint_file(), main(), _regex_matcher(), Rule, _use_effect_with_deps()

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (11): crop, dims, dir, interval, min, minMotion, refDur, reference (+3 more)

### Community 17 - "Community 17"
Cohesion: 0.22
Nodes (16): BGM_PY_DEPS, generateBgmDetached(), inferBgmPrompt(), LYRIA_PY_DEPS, lyriaKey(), musicgenScript(), pipInstall(), pyOk() (+8 more)

### Community 18 - "Community 18"
Cohesion: 0.11
Nodes (10): argv, audioMeta, audioMetaPath, base, hyperframesDir, intervalMs, outPath, started (+2 more)

### Community 19 - "Community 19"
Cohesion: 0.18
Nodes (13): argv, dur, output, positional, clone(), list(), main(), MEDIA_TYPES (+5 more)

### Community 20 - "Community 20"
Cohesion: 0.15
Nodes (16): dependencies, react@^18.3.1, react-dom@^18.3.1, remotion@^4.0.0, @remotion/cli@^4.0.0, zod@^4.6.6, react, react-dom (+8 more)

### Community 21 - "Community 21"
Cohesion: 0.15
Nodes (3): IndicatorResult, EMV, WR

### Community 22 - "Community 22"
Cohesion: 0.25
Nodes (5): compute_band_edges(), compute_fft_bands(), decode_audio(), extract(), main()

### Community 23 - "Community 23"
Cohesion: 0.23
Nodes (9): geminiAuth(), geminiConfigured(), GEMINI_TTS_MODEL, GEMINI_TTS_MODELS, pcmToWav(), synthesizeGemini(), withCause(), elevenlabsAvailable() (+1 more)

### Community 24 - "Community 24"
Cohesion: 0.17
Nodes (14): dependencies, react@^18.3.1, react-dom@^18.3.1, remotion@^4.0.0, @remotion/cli@^4.0.0, react, react-dom, remotion (+6 more)

### Community 25 - "Community 25"
Cohesion: 0.17
Nodes (14): dependencies, react@^18.3.1, react-dom@^18.3.1, remotion@^4.0.0, @remotion/cli@^4.0.0, react, react-dom, remotion (+6 more)

### Community 26 - "Community 26"
Cohesion: 0.14
Nodes (3): handle, CustomHookDriven(), useFadeIn()

### Community 27 - "Community 27"
Cohesion: 0.19
Nodes (4): clear_registry(), get_current_hour_timestamp(), IndicatorCategory, timestamp_to_date()

### Community 29 - "Community 29"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, isolatedModules, jsx, module, moduleResolution, resolveJsonModule (+4 more)

### Community 30 - "Community 30"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, isolatedModules, jsx, module, moduleResolution, resolveJsonModule (+4 more)

### Community 31 - "Community 31"
Cohesion: 0.15
Nodes (12): compilerOptions, esModuleInterop, forceConsistentCasingInFileNames, isolatedModules, jsx, module, moduleResolution, resolveJsonModule (+4 more)

### Community 32 - "Community 32"
Cohesion: 0.19
Nodes (3): IndicatorConfig, CCI, SuperTrend

### Community 33 - "Community 33"
Cohesion: 0.27
Nodes (6): _comparable(), _contains(), _expand_home(), _extensions(), find_program(), trusted_path_dirs()

### Community 34 - "Community 34"
Cohesion: 0.31
Nodes (6): isMainModule(), invocation(), manifests, npmFolder(), pluginVersion(), root

### Community 35 - "Community 35"
Cohesion: 0.24
Nodes (5): defaultProbe(), pythonCommand(), resolvePythonCommand(), posixOnly, withoutWorkingDirectory()

### Community 36 - "Community 36"
Cohesion: 0.29
Nodes (7): defaultProps, RemotionRoot(), StatsScene(), Props, TitleScene(), Stargazed(), stargazedSchema

### Community 37 - "Community 37"
Cohesion: 0.36
Nodes (3): generate_bgm(), main(), parse_args()

### Community 39 - "Community 39"
Cohesion: 0.31
Nodes (6): AnimatedNumber(), Props, Props, StatCard(), Props, Stat

### Community 40 - "Community 40"
Cohesion: 0.29
Nodes (5): guards, here, readdirTree(), scripts(), skillsRoot

### Community 42 - "Community 42"
Cohesion: 0.43
Nodes (5): ImageScene(), MultiScene(), OutroScene(), TitleScene(), RemotionRoot()

### Community 45 - "Community 45"
Cohesion: 0.38
Nodes (4): cutVideo(), fixture(), run(), SCRIPT

### Community 46 - "Community 46"
Cohesion: 0.57
Nodes (6): read_json_value(), require_render_tier_tools(), run_lint_tier(), run_render_tier(), run.sh script, write_result()

### Community 48 - "Community 48"
Cohesion: 0.40
Nodes (4): fixture(), program(), python, scripts

### Community 49 - "Community 49"
Cohesion: 0.40
Nodes (3): blocked, fetchMedia(), isPublicMediaUrl()

### Community 51 - "Community 51"
Cohesion: 0.47
Nodes (4): Props, UnderlinedText(), OutroScene(), Props

### Community 64 - "Community 64"
Cohesion: 0.40
Nodes (4): chime, description, duration, file

### Community 66 - "Community 66"
Cohesion: 0.50
Nodes (4): atempoChain(), parseWords(), scaleWords(), stretchToWav()

### Community 67 - "Community 67"
Cohesion: 0.70
Nodes (4): creditLimit(), creditsSpent(), read(), refuseUnderLimit()

### Community 68 - "Community 68"
Cohesion: 0.50
Nodes (4): click, description, duration, file

### Community 69 - "Community 69"
Cohesion: 0.50
Nodes (4): click-soft, description, duration, file

### Community 70 - "Community 70"
Cohesion: 0.50
Nodes (4): error, description, duration, file

### Community 71 - "Community 71"
Cohesion: 0.50
Nodes (4): glitch-1, description, duration, file

### Community 72 - "Community 72"
Cohesion: 0.50
Nodes (4): glitch-2, description, duration, file

### Community 73 - "Community 73"
Cohesion: 0.50
Nodes (4): glitch-3, description, duration, file

### Community 74 - "Community 74"
Cohesion: 0.50
Nodes (4): impact-bass-1, description, duration, file

### Community 75 - "Community 75"
Cohesion: 0.50
Nodes (4): impact-bass-2, description, duration, file

### Community 76 - "Community 76"
Cohesion: 0.50
Nodes (4): key-press, description, duration, file

### Community 77 - "Community 77"
Cohesion: 0.50
Nodes (4): notification, description, duration, file

### Community 78 - "Community 78"
Cohesion: 0.50
Nodes (4): ping, description, duration, file

### Community 79 - "Community 79"
Cohesion: 0.50
Nodes (4): pop, description, duration, file

### Community 80 - "Community 80"
Cohesion: 0.50
Nodes (4): riser, description, duration, file

### Community 81 - "Community 81"
Cohesion: 0.50
Nodes (4): sparkle, description, duration, file

### Community 82 - "Community 82"
Cohesion: 0.50
Nodes (4): typing, description, duration, file

### Community 83 - "Community 83"
Cohesion: 0.50
Nodes (4): whoosh, description, duration, file

### Community 84 - "Community 84"
Cohesion: 0.50
Nodes (4): whoosh-cinematic, description, duration, file

### Community 85 - "Community 85"
Cohesion: 0.50
Nodes (4): whoosh-short, description, duration, file

### Community 92 - "Community 92"
Cohesion: 0.83
Nodes (3): MyComposition(), pick(), TitleCard()

## Knowledge Gaps
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `IndicatorResult` connect `Community 21` to `Community 6`, `Community 9`, `Community 10`, `Community 27`, `Community 28`, `Community 32`, `Community 43`, `Community 44`, `Community 52`, `Community 53`, `Community 54`, `Community 55`, `Community 56`, `Community 57`, `Community 58`, `Community 59`, `Community 60`, `Community 61`, `Community 62`, `Community 63`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `IndicatorResult` (e.g. with `ATR` and `AVL`) actually correct?**
  _`IndicatorResult` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06829488919041157 - nodes in this community are weakly interconnected._
- **Why does `TechnicalUtils` connect `Community 9` to `Community 32`, `Community 59`, `Community 10`, `Community 44`, `Community 52`, `Community 53`, `Community 54`, `Community 55`, `Community 56`, `Community 21`, `Community 58`, `Community 27`, `Community 60`, `Community 63`, `Community 57`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `IndicatorConfig` (e.g. with `ATR` and `AVL`) actually correct?**
  _`IndicatorConfig` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.08315863032844165 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.09065679925994449 - nodes in this community are weakly interconnected._