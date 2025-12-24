---
layout: default
title: "PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence"
---

# PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16793" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16793v1</a>
  <a href="https://arxiv.org/pdf/2512.16793.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16793v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16793v1', 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaopeng Lin, Shijie Lian, Bin Yu, Ruoqi Yang, Changti Wu, Yuzhuo Miao, Yurun Jin, Yukun Shi, Cong Huang, Bojun Cheng, Kai Chen

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: 17 pages, 4 figures

---

## 💡 一句话要点

**提出PhysBrain，利用人类第一视角数据提升机器人物理智能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `第一视角视觉` `具身智能` `视觉语言模型` `迁移学习`

## 📋 核心要点

1. 现有VLM主要基于第三人称数据训练，与机器人第一视角存在视角差异，限制了机器人物理智能的发展。
2. 论文提出Egocentric2Embodiment翻译流程，将人类第一视角视频转化为多层次VQA监督，构建大规模E2E-3M数据集。
3. 通过在E2E-3M上训练PhysBrain，显著提升了机器人以自我为中心的理解能力，并在下游控制任务中取得更好效果。

## 📝 摘要（中文）

机器人泛化依赖于物理智能，即在第一视角感知和动作下，推理状态变化、富接触交互和长时程规划的能力。然而，大多数视觉语言模型（VLM）主要在第三人称数据上训练，这与人形机器人存在根本的视角不匹配。扩展机器人第一视角数据收集不切实际，因为成本高且多样性有限。大规模人类第一视角视频提供了一种可扩展的替代方案，自然地捕捉了丰富的交互上下文和因果结构。关键挑战是将原始第一视角视频转换为结构化且可靠的具身训练监督。为此，我们提出了一个Egocentric2Embodiment翻译流程，将第一人称视频转换为多层次、模式驱动的VQA监督，并强制执行证据 grounding 和时间一致性，从而大规模构建Egocentric2Embodiment数据集（E2E-3M）。通过在E2E-3M数据集上训练，获得了一个以自我为中心的具身大脑，称为PhysBrain。PhysBrain 显著提高了以自我为中心的理解能力，尤其是在 EgoThink 上的规划。它提供了一个以自我为中心的初始化，可以实现更高效的 VLA 微调和更高的 SimplerEnv 成功率（53.9%），证明了从人类以自我为中心的监督到下游机器人控制的有效迁移。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）主要在第三人称视角数据上训练，这与机器人需要的第一人称视角存在根本性的不匹配。这种视角差异阻碍了VLM在机器人控制任务中的应用，尤其是在需要物理交互和长时程规划的场景下。同时，直接收集大规模机器人第一视角数据成本高昂且多样性有限。

**核心思路**：论文的核心思路是利用大规模人类第一视角视频作为机器人训练的替代数据源。人类第一视角视频自然地捕捉了丰富的交互上下文和因果结构，可以为机器人提供有价值的具身学习监督信号。通过将人类第一视角视频转化为结构化的训练数据，可以弥合VLM与机器人之间的视角差异，提升机器人的物理智能。

**技术框架**：论文提出了一个名为Egocentric2Embodiment的翻译流程，该流程将第一人称视频转换为多层次、模式驱动的VQA监督。该流程包含以下几个主要步骤：1) 视频数据收集与预处理；2) 基于模式的VQA问题生成，包括状态变化、交互推理和长时程规划等方面；3) 证据 grounding，确保VQA答案与视频内容相关联；4) 时间一致性约束，保证VQA答案在时间上的连贯性。通过该流程，构建了大规模的Egocentric2Embodiment数据集（E2E-3M），用于训练PhysBrain。

**关键创新**：论文的关键创新在于提出了Egocentric2Embodiment翻译流程，该流程能够有效地将非结构化的第一人称视频转化为结构化的具身学习监督信号。与以往方法相比，该方法能够利用大规模人类数据，降低机器人数据收集成本，并提升训练数据的多样性。此外，论文还提出了PhysBrain，一个以自我为中心的具身大脑，能够更好地理解第一人称视角下的场景和任务。

**关键设计**：E2E-3M数据集包含300万个视频片段，每个片段都包含多层次的VQA问题。VQA问题的设计涵盖了状态变化、交互推理和长时程规划等多个方面，旨在全面提升机器人的物理智能。在训练PhysBrain时，使用了对比学习和掩码语言建模等技术，以提高模型的泛化能力和鲁棒性。具体参数设置和网络结构细节在论文中有详细描述，此处不再赘述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_pipeline.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_sum.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PhysBrain在EgoThink数据集上表现出显著的性能提升，证明了其在以自我为中心的理解能力方面的优势。此外，通过将PhysBrain作为初始化，VLA微调的效率更高，SimplerEnv的成功率也提升至53.9%，表明了从人类第一视角监督到下游机器人控制的有效迁移。

## 🎯 应用场景

该研究成果可应用于各种机器人控制任务，例如家庭服务机器人、工业机器人和医疗机器人。通过利用人类第一视角数据进行训练，可以显著提升机器人在复杂环境中的适应性和交互能力。未来，该方法有望推动机器人技术的发展，使其能够更好地服务于人类社会。

## 📄 摘要（原文）

> Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. However, most VLMs are trained primarily on third-person data, creating a fundamental viewpoint mismatch for humanoid robots. Scaling robot egocentric data collection remains impractical due to high cost and limited diversity, whereas large-scale human egocentric videos offer a scalable alternative that naturally capture rich interaction context and causal structure. The key challenge is to convert raw egocentric videos into structured and reliable embodiment training supervision. Accordingly, we propose an Egocentric2Embodiment translation pipeline that transforms first-person videos into multi-level, schema-driven VQA supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning on EgoThink. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher SimplerEnv success rates (53.9\%), demonstrating effective transfer from human egocentric supervision to downstream robot control.

