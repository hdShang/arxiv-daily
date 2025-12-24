---
layout: default
title: "DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models"
---

# DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05667" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05667v2</a>
  <a href="https://arxiv.org/pdf/2506.05667.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05667v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05667v2', 'DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhan Hao, Zhengning Li, Lei Sun, Weilong Wang, Naixin Yi, Sheng Song, Caihong Qin, Mofan Zhou, Yifei Zhan, Xianpeng Lang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-09-26)

**备注**: Benchmark: https://huggingface.co/datasets/LiAuto-DriveAction/drive-action

---

## 💡 一句话要点

**提出DriveAction基准以解决VLA模型决策多样性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-行动` `自动驾驶` `基准测试` `多模态学习` `动作预测` `评估框架` `真实世界数据`

## 📋 核心要点

1. 现有的VLA模型基准缺乏场景多样性和可靠的动作注释，限制了模型的实际应用。
2. DriveAction基准通过真实驾驶数据生成问答对，提供高质量的动作标签，并建立了树状评估框架。
3. 实验结果显示，视觉和语言输入对动作预测至关重要，缺失任一输入都会显著降低准确率。

## 📝 摘要（中文）

视觉-语言-行动（VLA）模型在自动驾驶领域取得了进展，但现有基准缺乏场景多样性、可靠的动作级别注释和与人类偏好一致的评估协议。为了解决这些问题，我们提出了DriveAction，这是第一个专门为VLA模型设计的以动作为驱动的基准，包含来自2610个驾驶场景的16185个问答对。DriveAction利用真实世界的驾驶数据，确保广泛且具有代表性的场景覆盖，提供直接来自驾驶员实际驾驶操作的高水平离散动作标签，并实施一个以动作为根的树状评估框架，明确链接视觉、语言和动作任务，支持全面和任务特定的评估。实验表明，最先进的视觉-语言模型（VLM）在准确的动作预测中需要视觉和语言的指导：没有视觉输入时，准确率平均下降3.3%；没有语言输入时下降4.1%；没有任何输入时下降8.0%。我们的评估支持精确识别模型瓶颈，提供新的见解和严格的基础，以推动自动驾驶中的类人决策。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有VLA模型基准在场景多样性、动作注释可靠性和评估协议一致性方面的不足，限制了模型的有效性和应用。

**核心思路**：提出DriveAction基准，通过真实世界的驾驶数据生成问答对，确保场景的广泛覆盖，并提供高质量的动作标签，进而实现更准确的动作预测。

**技术框架**：DriveAction的整体架构包括数据收集、问答对生成、动作标签标注和树状评估框架，明确链接视觉、语言和动作任务，支持全面评估。

**关键创新**：DriveAction是首个以动作为驱动的基准，创新性地结合了视觉、语言和动作任务的评估，填补了现有基准的空白。

**关键设计**：在数据收集阶段，采用真实驾驶数据，确保场景的多样性；在评估框架中，设计了树状结构以支持任务特定评估，确保评估结果的可靠性。

## 📊 实验亮点

实验结果表明，最先进的视觉-语言模型在缺失视觉输入时，准确率平均下降3.3%；缺失语言输入时下降4.1%；而缺失任一输入时，准确率下降高达8.0%。这些结果强调了视觉和语言输入在准确动作预测中的重要性。

## 🎯 应用场景

DriveAction基准可广泛应用于自动驾驶系统的开发与评估，帮助研究人员和工程师更好地理解和优化VLA模型的决策能力。未来，该基准有望推动更智能的自动驾驶技术，提升道路安全性和驾驶体验。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have advanced autonomous driving, but existing benchmarks still lack scenario diversity, reliable action-level annotation, and evaluation protocols aligned with human preferences. To address these limitations, we introduce DriveAction, the first action-driven benchmark specifically designed for VLA models, comprising 16,185 QA pairs generated from 2,610 driving scenarios. DriveAction leverages real-world driving data proactively collected by drivers of autonomous vehicles to ensure broad and representative scenario coverage, offers high-level discrete action labels collected directly from drivers' actual driving operations, and implements an action-rooted tree-structured evaluation framework that explicitly links vision, language, and action tasks, supporting both comprehensive and task-specific assessment. Our experiments demonstrate that state-of-the-art vision-language models (VLMs) require both vision and language guidance for accurate action prediction: on average, accuracy drops by 3.3% without vision input, by 4.1% without language input, and by 8.0% without either. Our evaluation supports precise identification of model bottlenecks with robust and consistent results, thus providing new insights and a rigorous foundation for advancing human-like decisions in autonomous driving.

