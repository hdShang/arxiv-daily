---
layout: default
title: "AdaTooler-V: Adaptive Tool-Use for Images and Videos"
---

# AdaTooler-V: Adaptive Tool-Use for Images and Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16918" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16918v1</a>
  <a href="https://arxiv.org/pdf/2512.16918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16918v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16918v1', 'AdaTooler-V: Adaptive Tool-Use for Images and Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page: https://github.com/CYWang735/AdaTooler-V

---

## 💡 一句话要点

**提出AdaTooler-V，通过自适应工具使用提升多模态大语言模型在图像和视频任务中的推理效率和性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `自适应工具使用` `强化学习` `视觉推理` `图像视频处理`

## 📋 核心要点

1. 现有多模态大语言模型存在盲目工具使用问题，即使不需要视觉工具也会调用，导致推理开销增加和性能下降。
2. AdaTooler-V通过AT-GRPO强化学习算法，根据工具收益自适应调整奖励尺度，鼓励模型仅在必要时调用工具。
3. 实验结果表明，AdaTooler-V在多个视觉推理任务中优于现有方法，并在高分辨率基准测试中超越了GPT-4o和Gemini 1.5 Pro。

## 📝 摘要（中文）

本文提出AdaTooler-V，一种多模态大语言模型（MLLM），通过自适应工具使用来解决现有开源模型中存在的盲目工具使用问题。现有模型即使在不需要视觉工具的情况下也会调用，从而显著增加推理开销并降低模型性能。AdaTooler-V通过AT-GRPO强化学习算法自适应地调整奖励尺度，鼓励模型仅在工具能带来真正改进时才调用。此外，构建了AdaTooler-V-CoT-100k和AdaTooler-V-300k两个数据集，分别用于SFT冷启动和RL训练，涵盖单图像、多图像和视频数据。在十二个基准测试上的实验表明，AdaTooler-V具有强大的推理能力，在各种视觉推理任务中优于现有方法。值得注意的是，AdaTooler-V-7B在高分辨率基准V*上实现了89.8%的准确率，超过了商业专有模型GPT-4o和Gemini 1.5 Pro。所有代码、模型和数据均已发布。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在视觉任务中盲目使用工具的问题。现有开源MLLMs常常不加区分地调用视觉工具，即使这些工具对于解决当前问题并非必要。这种盲目性导致了不必要的计算开销，降低了推理效率，并且可能损害模型的整体性能。因此，如何让MLLMs学会自适应地判断何时需要使用工具，以及何时可以避免使用工具，是本文要解决的核心问题。

**核心思路**：论文的核心思路是训练模型仅在工具能够带来显著性能提升时才调用工具。为了实现这一目标，论文引入了一种基于强化学习的训练方法，该方法通过奖励机制来鼓励模型进行合理的工具使用决策。具体来说，模型会根据工具的使用情况获得奖励，如果使用工具能够显著提高解决问题的准确性，则会获得更高的奖励；反之，如果使用工具并没有带来明显的改进，则会受到惩罚。通过这种方式，模型可以逐渐学习到何时应该使用工具，以及何时应该避免使用工具。

**技术框架**：AdaTooler-V的整体框架包含以下几个主要组成部分：1) 多模态大语言模型（MLLM）：作为模型的核心，负责接收输入（图像、视频和文本），并生成输出（文本）。2) 视觉工具：提供各种视觉处理能力，例如目标检测、图像分割等。3) AT-GRPO强化学习算法：用于训练模型，使其能够自适应地选择是否使用视觉工具。4) 奖励函数：用于评估模型使用工具的效果，并根据效果给予奖励或惩罚。训练过程包括：首先使用AdaTooler-V-CoT-100k数据集进行监督微调（SFT），为模型提供一个良好的冷启动。然后，使用AdaTooler-V-300k数据集进行强化学习训练，通过AT-GRPO算法优化模型，使其能够自适应地选择是否使用工具。

**关键创新**：论文的关键创新在于提出了AT-GRPO（Adaptive Tool-use with Gradient Ratio Policy Optimization）强化学习算法。该算法的核心思想是根据每个样本的“工具收益分数”（Tool Benefit Score）自适应地调整奖励尺度。工具收益分数衡量了使用工具相比不使用工具所带来的性能提升。如果工具收益分数较高，则模型在使用工具时会获得更高的奖励，从而鼓励模型在必要时使用工具。与传统的强化学习算法相比，AT-GRPO能够更有效地引导模型学习合理的工具使用策略。

**关键设计**：AT-GRPO算法的关键设计在于奖励尺度的自适应调整。具体来说，奖励尺度与工具收益分数成正比。工具收益分数可以通过比较模型在使用工具和不使用工具两种情况下的性能来估计。此外，论文还设计了两个数据集AdaTooler-V-CoT-100k和AdaTooler-V-300k，用于支持模型的训练。AdaTooler-V-CoT-100k数据集包含10万个样本，用于SFT冷启动。AdaTooler-V-300k数据集包含30万个样本，用于强化学习训练，并提供了可验证的奖励信号。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16918v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AdaTooler-V在十二个基准测试中表现出色，证明了其强大的视觉推理能力。尤其是在高分辨率基准V*上，AdaTooler-V-7B达到了89.8%的准确率，超越了商业专有模型GPT-4o和Gemini 1.5 Pro。这表明AdaTooler-V在处理复杂视觉任务方面具有显著优势。

## 🎯 应用场景

AdaTooler-V具有广泛的应用前景，例如智能客服、自动驾驶、医疗诊断等领域。在智能客服中，模型可以根据用户提供的图像或视频，自动选择合适的视觉工具进行分析，从而更准确地理解用户的问题并提供相应的解决方案。在自动驾驶中，模型可以利用视觉工具来识别交通标志、行人和其他车辆，从而提高驾驶安全性。在医疗诊断中，模型可以分析医学图像，辅助医生进行疾病诊断。

## 📄 摘要（原文）

> Recent advances have shown that multimodal large language models (MLLMs) benefit from multimodal interleaved chain-of-thought (CoT) with vision tool interactions. However, existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary, which significantly increases inference overhead and degrades model performance. To this end, we propose AdaTooler-V, an MLLM that performs adaptive tool-use by determining whether a visual problem truly requires tools. First, we introduce AT-GRPO, a reinforcement learning algorithm that adaptively adjusts reward scales based on the Tool Benefit Score of each sample, encouraging the model to invoke tools only when they provide genuine improvements. Moreover, we construct two datasets to support training: AdaTooler-V-CoT-100k for SFT cold start and AdaTooler-V-300k for RL with verifiable rewards across single-image, multi-image, and video data. Experiments across twelve benchmarks demonstrate the strong reasoning capability of AdaTooler-V, outperforming existing methods in diverse visual reasoning tasks. Notably, AdaTooler-V-7B achieves an accuracy of 89.8\% on the high-resolution benchmark V*, surpassing the commercial proprietary model GPT-4o and Gemini 1.5 Pro. All code, models, and data are released.

