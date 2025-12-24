---
layout: default
title: "Scientists' First Exam: Probing Cognitive Abilities of MLLM via Perception, Understanding, and Reasoning"
---

# Scientists' First Exam: Probing Cognitive Abilities of MLLM via Perception, Understanding, and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10521" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10521v6</a>
  <a href="https://arxiv.org/pdf/2506.10521.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10521v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10521v6', 'Scientists\' First Exam: Probing Cognitive Abilities of MLLM via Perception, Understanding, and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhao Zhou, Yiheng Wang, Xuming He, Ao Shen, Ruoyao Xiao, Zhiwei Li, Qiantai Feng, Zijie Guo, Yuejin Yang, Hao Wu, Wenxuan Huang, Jiaqi Wei, Dan Si, Xiuqi Yao, Jia Bu, Haiwen Huang, Manning Wang, Tianfan Fu, Shixiang Tang, Ben Fei, Dongzhan Zhou, Fenghua Ling, Yan Lu, Siqi Sun, Chenhui Li, Guanjie Zheng, Jiancheng Lv, Wenlong Zhang, Lei Bai

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-12 (更新: 2025-11-14)

**备注**: 82 pages

---

## 💡 一句话要点

**提出科学家首考基准以评估多模态大语言模型的认知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `科学推理` `认知能力评估` `视觉问答` `科学发现` `基准测试` `人工智能`

## 📋 核心要点

1. 现有科学基准主要关注MLLMs的知识理解能力，忽视了其感知和推理能力的评估，导致评估不全面。
2. 本文提出科学家首考（SFE）基准，通过科学信号感知、属性理解和比较推理三个层面评估MLLMs的认知能力。
3. 实验结果显示，当前最先进的模型在SFE基准上表现不佳，表明在科学推理方面仍有很大的改进空间。

## 📝 摘要（中文）

科学发现越来越依赖于基于信息密集型科学数据和领域特定专业知识的复杂多模态推理。借助专家级科学基准，多模态大语言模型（MLLMs）有潜力显著提升这一发现过程。然而，现有科学基准主要集中在评估MLLMs的知识理解能力，导致对其感知和推理能力的评估不足。为了解决这一问题，本文提出了科学家首考（SFE）基准，旨在通过科学信号感知、科学属性理解和科学比较推理三个相互关联的层面评估MLLMs的科学认知能力。SFE包含830个专家验证的视觉问答对，涵盖66个多模态任务，涉及五个高价值学科。实验结果显示，当前最先进的GPT-o3和InternVL-3在SFE上仅获得34.08%和26.52%的成绩，表明MLLMs在科学领域仍有显著提升空间。

## 🔬 方法详解

**问题定义**：本文旨在解决现有科学基准对多模态大语言模型（MLLMs）评估的不足，特别是对其感知和推理能力的评估缺失。现有方法主要集中在知识理解，导致无法全面评估模型的科学认知能力。

**核心思路**：论文提出科学家首考（SFE）基准，设计了三个层面来评估MLLMs的科学认知能力，包括科学信号感知、科学属性理解和科学比较推理，旨在全面评估模型的多模态推理能力。

**技术框架**：SFE基准包含830个专家验证的视觉问答对，覆盖66个多模态任务，涉及五个高价值学科。评估过程通过三个层面进行，确保模型在不同科学任务中的表现得到全面考量。

**关键创新**：SFE基准的创新在于其多层次的评估框架，首次将科学信号感知、属性理解和比较推理结合在一起，提供了更全面的评估标准，与现有方法相比，能够更好地反映模型在科学领域的实际能力。

**关键设计**：在设计SFE时，采用了专家验证的问答对，确保问题的科学性和准确性。同时，任务覆盖了多个学科，增强了评估的广泛性和适用性。

## 📊 实验亮点

实验结果显示，当前最先进的GPT-o3和InternVL-3在SFE基准上仅获得34.08%和26.52%的成绩，表明在科学推理方面仍有显著提升空间。这一发现强调了进一步研究和改进MLLMs在科学领域应用的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、教育和智能助手等。通过提升多模态大语言模型的认知能力，能够更好地支持科学发现和决策过程，推动科学研究的进展。未来，SFE基准有望成为评估AI在科学领域应用的重要标准。

## 📄 摘要（原文）

> Scientific discoveries increasingly rely on complex multimodal reasoning based on information-intensive scientific data and domain-specific expertise. Empowered by expert-level scientific benchmarks, scientific Multimodal Large Language Models (MLLMs) hold the potential to significantly enhance this discovery process in realistic workflows. However, current scientific benchmarks mostly focus on evaluating the knowledge understanding capabilities of MLLMs, leading to an inadequate assessment of their perception and reasoning abilities. To address this gap, we present the Scientists' First Exam (SFE) benchmark, designed to evaluate the scientific cognitive capacities of MLLMs through three interconnected levels: scientific signal perception, scientific attribute understanding, scientific comparative reasoning. Specifically, SFE comprises 830 expert-verified VQA pairs across three question types, spanning 66 multimodal tasks across five high-value disciplines. Extensive experiments reveal that current state-of-the-art GPT-o3 and InternVL-3 achieve only 34.08% and 26.52% on SFE, highlighting significant room for MLLMs to improve in scientific realms. We hope the insights obtained in SFE will facilitate further developments in AI-enhanced scientific discoveries.

