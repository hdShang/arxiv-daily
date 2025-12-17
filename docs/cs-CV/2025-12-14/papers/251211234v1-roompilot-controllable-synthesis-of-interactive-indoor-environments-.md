---
layout: default
title: RoomPilot: Controllable Synthesis of Interactive Indoor Environments via Multimodal Semantic Parsing
---

# RoomPilot: Controllable Synthesis of Interactive Indoor Environments via Multimodal Semantic Parsing

**arXiv**: [2512.11234v1](https://arxiv.org/abs/2512.11234) | [PDF](https://arxiv.org/pdf/2512.11234.pdf)

**作者**: Wentang Chen, Shougao Zhang, Yiman Zhang, Tianhao Zhou, Ruihui Li

---

## 💡 一句话要点

**提出RoomPilot框架，通过多模态语义解析实现可控交互式室内场景合成**

**关键词**: `室内场景生成` `多模态语义解析` `可控合成` `交互式环境` `领域特定语言`

## 📋 核心要点

1. 核心问题：现有方法输入模态有限或依赖随机过程，难以生成可控交互式室内场景。
2. 方法要点：设计室内领域特定语言（IDSL）作为共享语义表示，解析文本或CAD平面图以生成结构化场景。
3. 实验或效果：验证了多模态理解能力、细粒度可控性，以及物理一致性和视觉保真度的提升。

## 📄 摘要（原文）

> Generating controllable and interactive indoor scenes is fundamental to applications in game development, architectural visualization, and embodied AI training. Yet existing approaches either handle a narrow range of input modalities or rely on stochastic processes that hinder controllability. To overcome these limitations, we introduce RoomPilot, a unified framework that parses diverse multi-modal inputs--textual descriptions or CAD floor plans--into an Indoor Domain-Specific Language (IDSL) for indoor structured scene generation. The key insight is that a well-designed IDSL can act as a shared semantic representation, enabling coherent, high-quality scene synthesis from any single modality while maintaining interaction semantics. In contrast to conventional procedural methods that produce visually plausible but functionally inert layouts, RoomPilot leverages a curated dataset of interaction-annotated assets to synthesize environments exhibiting realistic object behaviors. Extensive experiments further validate its strong multi-modal understanding, fine-grained controllability in scene generation, and superior physical consistency and visual fidelity, marking a significant step toward general-purpose controllable 3D indoor scene generation.

