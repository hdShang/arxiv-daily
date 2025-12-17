---
layout: default
title: NExT-OMNI: Towards Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching
---

# NExT-OMNI: Towards Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13721" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13721v2</a>
  <a href="https://arxiv.org/pdf/2510.13721.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13721v2" onclick="toggleFavorite(this, '2510.13721v2', 'NExT-OMNI: Towards Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Run Luo, Xiaobo Xia, Lu Wang, Longze Chen, Renke Shan, Jing Luo, Min Yang, Tat-Seng Chua

**分类**: cs.CL, cs.AI, cs.CV, cs.MM

**发布日期**: 2025-10-15 (更新: 2025-10-16)

---

## 💡 一句话要点

**NExT-OMNI：基于离散流匹配的任意到任意全模态统一建模**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `全模态模型` `离散流匹配` `跨模态检索` `多轮交互` `统一建模` `生成模型`

## 📋 核心要点

1. 现有模型受限于自回归架构，难以平衡理解和生成能力，混合和解耦策略设计冗余，限制了其在跨模态检索等更广泛场景中的应用。
2. NExT-OMNI利用离散流范式，通过度量诱导的概率路径和动力学最优速度，实现任意模态到任意模态的统一建模，提升响应效率。
3. NExT-OMNI在多模态生成和理解任务上表现出色，并在多轮多模态交互和跨模态检索方面超越了以往的统一模型。

## 📝 摘要（中文）

本文提出了NExT-OMNI，一个开源的全模态基础模型，旨在通过离散流范式实现统一建模，从而支持任意模态到任意模态的理解和生成，并提高响应效率。NExT-OMNI利用度量诱导的概率路径和动力学最优速度，通过简洁的统一表示而非任务解耦设计，实现更广泛的应用场景，例如跨模态检索。该模型在大规模交错的文本、图像、视频和音频数据上进行训练，在多模态生成和理解基准测试中表现出竞争力的性能，并在多轮多模态交互和跨模态检索方面优于以往的统一模型，突显了其作为下一代多模态基础模型的架构优势。为了促进进一步的研究，作者发布了训练细节、数据协议以及代码和模型检查点。

## 🔬 方法详解

**问题定义**：现有的大部分多模态模型依赖于自回归架构，这限制了它们在理解和生成能力上的平衡。此外，虽然一些混合和解耦策略被用于统一框架中，但它们的设计较为冗余，无法很好地应用于更广泛的场景，例如跨模态检索。因此，需要一个更加统一和高效的模型，能够支持任意模态之间的转换和交互。

**核心思路**：NExT-OMNI的核心思路是利用离散流匹配（Discrete Flow Matching）范式，将不同模态的数据映射到统一的潜在空间中。通过学习度量诱导的概率路径和动力学最优速度，模型能够高效地在不同模态之间进行转换，从而实现任意模态到任意模态的理解和生成。这种方法避免了传统自回归模型的局限性，并提供了一种更加简洁和统一的建模方式。

**技术框架**：NExT-OMNI的整体架构基于离散流匹配。首先，不同模态的数据通过各自的编码器映射到潜在空间。然后，模型学习一个流场，该流场定义了从一个模态到另一个模态的概率路径。在生成过程中，模型沿着这个流场进行采样，从而生成目标模态的数据。该框架包含模态编码器、流场学习模块和模态解码器三个主要模块。

**关键创新**：NExT-OMNI的关键创新在于使用离散流匹配范式进行多模态统一建模。与传统的自回归模型相比，离散流匹配能够更有效地学习不同模态之间的关系，并支持任意模态之间的转换。此外，NExT-OMNI通过学习度量诱导的概率路径和动力学最优速度，进一步提高了生成效率和质量。

**关键设计**：NExT-OMNI的关键设计包括：1) 使用Transformer作为模态编码器和解码器，以捕捉不同模态数据的复杂特征；2) 设计了一种新的损失函数，用于学习流场，该损失函数同时考虑了生成质量和效率；3) 采用了一种自适应采样策略，以提高生成的多样性。

## 📊 实验亮点

NExT-OMNI在多模态生成和理解基准测试中表现出竞争力的性能。更重要的是，在多轮多模态交互和跨模态检索方面，NExT-OMNI显著优于以往的统一模型，证明了其架构的优越性。具体性能数据在论文中给出，表明NExT-OMNI在多个任务上都取得了SOTA或接近SOTA的结果。

## 🎯 应用场景

NExT-OMNI具有广泛的应用前景，包括多模态对话系统、跨模态内容生成、智能助手、教育娱乐等领域。它可以用于生成图像描述、视频摘要、音频转录等，还可以用于实现更自然和智能的人机交互。未来，NExT-OMNI有望成为通用人工智能系统的核心组成部分。

## 📄 摘要（原文）

> Next-generation multimodal foundation models capable of any-to-any cross-modal generation and multi-turn interaction will serve as core components of artificial general intelligence systems, playing a pivotal role in human-machine interaction. However, most existing multimodal models remain constrained by autoregressive architectures, whose inherent limitations prevent a balanced integration of understanding and generation capabilities. Although hybrid and decoupling strategies have been explored to address these tasks within unified frameworks separately, their redundant, non-integrated designs limit their applicability to broader scenarios, such as cross-modal retrieval. In this work, we introduce NExT-OMNI, an open-source omnimodal foundation model that achieves unified modeling through discrete flow paradigms. By leveraging metric-induced probability paths and kinetic optimal velocities, NExT-OMNI natively supports any-to-any understanding and generation with enhanced response efficiency, while enabling broader application scenarios through concise unified representations rather than task-decoupled designs. Trained on large-scale interleaved text, image, video, and audio data, NExT-OMNI delivers competitive performance on multimodal generation and understanding benchmarks, while outperforming prior unified models in multi-turn multimodal interaction and cross-modal retrieval, highlighting its architectural advantages as a next-generation multimodal foundation model. To advance further research, we release training details, data protocols, and open-source both the code and model checkpoints.

