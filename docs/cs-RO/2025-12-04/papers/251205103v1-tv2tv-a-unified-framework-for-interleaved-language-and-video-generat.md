---
layout: default
title: TV2TV: A Unified Framework for Interleaved Language and Video Generation
---

# TV2TV: A Unified Framework for Interleaved Language and Video Generation

**arXiv**: [2512.05103v1](https://arxiv.org/abs/2512.05103) | [PDF](https://arxiv.org/pdf/2512.05103.pdf)

**作者**: Xiaochuang Han, Youssef Emad, Melissa Hall, John Nguyen, Karthik Padthe, Liam Robbins, Amir Bar, Delong Chen, Michal Drozdzal, Maha Elbayad, Yushi Hu, Shang-Wen Li, Sreya Dutta Roy, Jakob Verbeek, XuDong Wang, Marjan Ghazvininejad, Luke Zettlemoyer, Emily Dinan

---

## 💡 一句话要点

**提出TV2TV框架，通过交错文本与视频生成提升复杂视频生成的质量与可控性。**

**关键词**: `视频生成` `语言建模` `流匹配` `交错生成` `可控生成` `混合Transformer`

## 📋 核心要点

1. 视频生成模型在复杂语义分支或高层推理场景中仍面临挑战。
2. TV2TV采用混合Transformer架构，联合学习语言建模与视频流匹配，实现交错生成。
3. 在视频游戏和体育视频实验中，TV2TV显著提升视觉质量和提示对齐，增强可控性。

## 📄 摘要（原文）

> Video generation models are rapidly advancing, but can still struggle with complex video outputs that require significant semantic branching or repeated high-level reasoning about what should happen next. In this paper, we introduce a new class of omni video-text models that integrate ideas from recent LM reasoning advances to address this challenge. More specifically, we present TV2TV, a unified generative modeling framework which decomposes video generation into an interleaved text and video generation process. TV2TV jointly learns language modeling (next-token prediction) and video flow matching (next-frame prediction) using a Mixture-of-Transformers (MoT) architecture. At inference time, TV2TV decides when to alternate between generating text and video frames, allowing the model to "think in words" about subsequent content before ``acting in pixels'' to produce frames. This design offloads much of the responsibility for deciding what should happen next to the language modeling tower, enabling improved visual quality and prompt alignment of generated videos. It also enables fine-grained controllability, allowing users to modify the video generation trajectory through text interventions at any point in the process. In controlled experiments on video game data, TV2TV demonstrates substantial improvements in both visual quality and controllability. TV2TV also scales to natural videos, as we show by augmenting sports videos with interleaved natural language action descriptions using vision-language models (VLMs). Training TV2TV on this corpus yields strong visual quality and prompt alignment, showcasing the model's ability to reason about and generate complex real-world action sequences. Together, these results highlight TV2TV as a promising step toward video generation with open-ended textual reasoning and control.

