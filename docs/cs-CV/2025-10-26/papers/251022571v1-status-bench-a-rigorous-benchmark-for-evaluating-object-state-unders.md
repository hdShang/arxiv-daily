---
layout: default
title: "STATUS Bench: A Rigorous Benchmark for Evaluating Object State Understanding in Vision-Language Models"
---

# STATUS Bench: A Rigorous Benchmark for Evaluating Object State Understanding in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22571" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22571v1</a>
  <a href="https://arxiv.org/pdf/2510.22571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22571v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22571v1', 'STATUS Bench: A Rigorous Benchmark for Evaluating Object State Understanding in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahiro Ukai, Shuhei Kurita, Nakamasa Inoue

**分类**: cs.CV, cs.AI, cs.MM

**发布日期**: 2025-10-26

---

## 💡 一句话要点

**STATUS Bench：用于评估视觉-语言模型物体状态理解能力的严格基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `物体状态识别` `基准数据集` `多模态学习` `图像检索`

## 📋 核心要点

1. 现有视觉-语言模型在物体状态识别方面能力不足，难以捕捉细微的状态变化，缺乏系统性的评估基准。
2. 提出 STATUS Bench，包含物体状态识别、图像检索和状态变化识别三个任务，全面评估模型对物体状态的理解能力。
3. 构建大规模训练数据集 STATUS Train，并验证了 STATUS Bench 的有效性，开源模型微调后性能显著提升。

## 📝 摘要（中文）

物体状态识别旨在识别物体的特定条件，例如其位置状态（例如，打开或关闭）和功能状态（例如，开启或关闭）。尽管最近的视觉-语言模型（VLMs）能够执行各种多模态任务，但它们在识别物体状态方面的精确程度仍不清楚。为了解决这个问题，我们引入了状态和转换理解基准（STATUS Bench），这是第一个严格评估 VLM 在不同情况下理解物体状态细微变化能力的基准。具体来说，STATUS Bench 引入了一种新颖的评估方案，要求 VLM 同时执行三项任务：物体状态识别（OSI）、图像检索（IR）和状态变化识别（SCI）。这些任务是在我们完全手工制作的数据集上定义的，该数据集涉及图像对、其相应的物体状态描述和状态变化描述。此外，我们引入了一个大规模训练数据集，即 STATUS Train，它由 1300 万个半自动创建的描述组成。该数据集是促进该领域进一步研究的最大资源。在我们的实验中，我们证明了 STATUS Bench 能够进行严格的一致性评估，并揭示了当前最先进的 VLM 仍然难以捕捉细微的物体状态差异。令人惊讶的是，在所提出的严格评估方案下，大多数开源 VLM 表现出接近随机水平的零样本性能。在 STATUS Train 上进行微调后，Qwen2.5-VL 实现了与 Gemini 2.0 Flash 相当的性能。这些发现强调了 STATUS Bench 和 Train 对于推进 VLM 研究中物体状态识别的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言模型（VLMs）在理解物体状态方面的不足。现有方法难以精确识别物体状态的细微变化，缺乏一个专门用于评估VLM物体状态理解能力的基准。这使得我们难以系统地评估和提升VLM在此方面的能力。

**核心思路**：论文的核心思路是构建一个专门的基准数据集 STATUS Bench，并设计一套严格的评估方案，迫使VLM同时执行物体状态识别（OSI）、图像检索（IR）和状态变化识别（SCI）三项任务。这种多任务联合评估的方式能够更全面、更严格地考察VLM对物体状态的理解能力。

**技术框架**：STATUS Bench 的整体框架包含两个主要部分：数据集构建和评估方案设计。数据集 STATUS Bench 包含手工标注的图像对，以及对应的物体状态描述和状态变化描述。评估方案要求VLM同时完成 OSI、IR 和 SCI 三个任务。OSI 任务要求模型识别图像中物体的状态；IR 任务要求模型根据状态描述检索对应的图像；SCI 任务要求模型识别图像对中物体状态的变化。

**关键创新**：论文的关键创新在于提出了一个新颖的评估方案，该方案通过多任务联合评估的方式，能够更全面、更严格地考察VLM对物体状态的理解能力。此外，论文还构建了一个大规模的训练数据集 STATUS Train，为VLM的训练提供了充足的数据支持。

**关键设计**：STATUS Bench 的关键设计包括：1) 精心挑选的图像对，涵盖了各种常见的物体状态和状态变化；2) 详细的物体状态描述和状态变化描述，为模型提供了丰富的语义信息；3) 多任务联合评估方案，迫使模型同时考虑物体状态的多个方面；4) 大规模训练数据集 STATUS Train，用于微调VLM，提升其物体状态理解能力。具体参数设置和网络结构取决于所使用的VLM模型，论文主要关注基准数据集和评估方案的设计。

## 📊 实验亮点

实验结果表明，现有的开源 VLM 在 STATUS Bench 上表现不佳，零样本性能接近随机水平，表明它们在物体状态理解方面存在明显不足。经过在 STATUS Train 上进行微调后，Qwen2.5-VL 的性能显著提升，达到了与 Gemini 2.0 Flash 相当的水平，验证了 STATUS Bench 和 Train 的有效性。

## 🎯 应用场景

该研究成果可应用于智能家居、机器人导航、自动驾驶等领域。例如，智能家居系统可以利用物体状态识别技术来判断家电设备的状态（如灯是否打开、门是否关闭），从而实现更智能化的控制。机器人可以利用该技术来理解周围环境，并根据物体状态的变化做出相应的动作。自动驾驶系统可以利用该技术来识别交通信号灯的状态，从而做出正确的驾驶决策。

## 📄 摘要（原文）

> Object state recognition aims to identify the specific condition of objects, such as their positional states (e.g., open or closed) and functional states (e.g., on or off). While recent Vision-Language Models (VLMs) are capable of performing a variety of multimodal tasks, it remains unclear how precisely they can identify object states. To alleviate this issue, we introduce the STAte and Transition UnderStanding Benchmark (STATUS Bench), the first benchmark for rigorously evaluating the ability of VLMs to understand subtle variations in object states in diverse situations. Specifically, STATUS Bench introduces a novel evaluation scheme that requires VLMs to perform three tasks simultaneously: object state identification (OSI), image retrieval (IR), and state change identification (SCI). These tasks are defined over our fully hand-crafted dataset involving image pairs, their corresponding object state descriptions and state change descriptions. Furthermore, we introduce a large-scale training dataset, namely STATUS Train, which consists of 13 million semi-automatically created descriptions. This dataset serves as the largest resource to facilitate further research in this area. In our experiments, we demonstrate that STATUS Bench enables rigorous consistency evaluation and reveal that current state-of-the-art VLMs still significantly struggle to capture subtle object state distinctions. Surprisingly, under the proposed rigorous evaluation scheme, most open-weight VLMs exhibited chance-level zero-shot performance. After fine-tuning on STATUS Train, Qwen2.5-VL achieved performance comparable to Gemini 2.0 Flash. These findings underscore the necessity of STATUS Bench and Train for advancing object state recognition in VLM research.

