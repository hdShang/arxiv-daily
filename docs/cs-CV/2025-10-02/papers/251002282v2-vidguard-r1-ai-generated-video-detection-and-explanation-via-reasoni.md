---
layout: default
title: VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL
---

# VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02282" target="_blank" class="toolbar-btn">arXiv: 2510.02282v2</a>
    <a href="https://arxiv.org/pdf/2510.02282.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02282v2" 
            onclick="toggleFavorite(this, '2510.02282v2', 'VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kyoungjun Park, Yifan Yang, Juheon Yi, Shicheng Zheng, Yifei Shen, Dongqi Han, Caihua Shan, Muhammad Muaz, Lili Qiu

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-02 (更新: 2025-10-06)

---

## 💡 一句话要点

**VidGuard-R1：利用推理MLLM和强化学习进行AI生成视频检测与解释**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成视频检测` `多模态大语言模型` `强化学习` `可解释性` `组相对策略优化`

## 📋 核心要点

1. 现有AI生成视频检测方法缺乏可解释性，难以满足监管和用户对透明度的需求。
2. VidGuard-R1通过组相对策略优化（GRPO）微调多模态大语言模型，实现准确检测和可解释推理。
3. 实验表明，VidGuard-R1在零样本设置下达到SOTA，经过训练后准确率超过95%，并能提供精确的解释。

## 📝 摘要（中文）

随着AI生成视频的快速发展，迫切需要有效的检测工具来减轻诸如虚假信息和声誉损害等社会风险。除了准确的分类之外，检测模型提供可解释的解释对于确保监管机构和最终用户的透明度至关重要。为了应对这些挑战，我们推出了VidGuard-R1，这是第一个视频真实性检测器，它使用组相对策略优化（GRPO）微调多模态大型语言模型（MLLM）。我们的模型提供高度准确的判断和深刻的推理。我们精心策划了一个具有挑战性的数据集，其中包含由最先进的生成模型生成的14万个真实和AI生成的视频，并仔细设计了生成过程以最大限度地提高区分难度。然后，我们使用GRPO和两个专门的奖励模型（针对时间伪影和生成复杂性）来微调Qwen-VL。大量实验表明，VidGuard-R1在现有基准测试中实现了最先进的零样本性能，额外的训练将准确率提高到95%以上。案例研究进一步表明，VidGuard-R1产生了其预测背后精确且可解释的基本原理。代码已在https://VidGuard-R1.github.io上公开发布。

## 🔬 方法详解

**问题定义**：当前AI生成视频检测方法主要关注准确率，但缺乏对检测结果的解释能力，导致用户难以信任检测结果，也给监管带来挑战。现有方法难以有效区分真实视频和复杂AI生成视频，尤其是在时间一致性和生成复杂性方面。

**核心思路**：VidGuard-R1的核心思路是利用多模态大语言模型（MLLM）的推理能力，结合强化学习，使其不仅能判断视频真伪，还能给出判断依据。通过奖励模型引导MLLM关注视频中的时间伪影和生成复杂性，从而提高检测准确率和可解释性。

**技术框架**：VidGuard-R1的整体框架包括：1) 数据集构建：构建包含真实和AI生成视频的大规模数据集，并着重提高生成难度；2) MLLM微调：使用组相对策略优化（GRPO）微调Qwen-VL模型；3) 奖励模型：训练两个奖励模型，分别评估视频的时间伪影和生成复杂性；4) 推理生成：利用微调后的MLLM生成视频真伪的判断和解释。

**关键创新**：VidGuard-R1的关键创新在于：1) 首次将强化学习引入AI生成视频检测领域，通过奖励模型引导MLLM学习；2) 提出组相对策略优化（GRPO）方法，提高训练效率和稳定性；3) 实现了既能准确检测，又能提供可解释推理的视频真实性检测器。

**关键设计**：GRPO的具体实现细节包括：定义奖励函数，鼓励模型关注时间伪影和生成复杂性；设计合适的prompt模板，引导MLLM生成清晰的解释；使用Qwen-VL作为基础模型，利用其强大的多模态理解能力。奖励模型的设计也至关重要，需要能够准确评估视频的时间一致性和生成难度。

## 📊 实验亮点

VidGuard-R1在现有基准测试中实现了最先进的零样本性能，无需额外训练即可达到SOTA水平。经过针对时间伪影和生成复杂性的训练后，准确率进一步提升至95%以上。案例研究表明，VidGuard-R1能够生成精确且可解释的推理，为用户提供可信的判断依据。

## 🎯 应用场景

VidGuard-R1可应用于社交媒体平台、新闻媒体机构等，用于检测和标记AI生成的虚假视频，防止虚假信息传播，维护网络安全。该技术还可用于版权保护，识别未经授权的AI生成内容。未来，该技术有望成为内容审核的重要组成部分，提升内容平台的公信力。

## 📄 摘要（原文）

> With the rapid advancement of AI-generated videos, there is an urgent need for effective detection tools to mitigate societal risks such as misinformation and reputational harm. In addition to accurate classification, it is essential that detection models provide interpretable explanations to ensure transparency for regulators and end users. To address these challenges, we introduce VidGuard-R1, the first video authenticity detector that fine-tunes a multi-modal large language model (MLLM) using group relative policy optimization (GRPO). Our model delivers both highly accurate judgments and insightful reasoning. We curate a challenging dataset of 140k real and AI-generated videos produced by state-of-the-art generation models, carefully designing the generation process to maximize discrimination difficulty. We then fine-tune Qwen-VL using GRPO with two specialized reward models that target temporal artifacts and generation complexity. Extensive experiments demonstrate that VidGuard-R1 achieves state-of-the-art zero-shot performance on existing benchmarks, with additional training pushing accuracy above 95%. Case studies further show that VidGuard-R1 produces precise and interpretable rationales behind its predictions. The code is publicly available at https://VidGuard-R1.github.io.

