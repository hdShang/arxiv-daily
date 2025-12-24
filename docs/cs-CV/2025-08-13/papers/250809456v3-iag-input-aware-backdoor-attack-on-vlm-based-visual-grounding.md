---
layout: default
title: "IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding"
---

# IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09456" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09456v3</a>
  <a href="https://arxiv.org/pdf/2508.09456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09456v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09456v3', 'IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junxian Li, Beining Xu, Simin Chen, Jiatong Li, Jingdi Lei, Haodong Zhao, Di Zhang

**分类**: cs.CV, cs.CL, cs.CR

**发布日期**: 2025-08-13 (更新: 2025-11-24)

**备注**: 20 pages, 13 Figures

---

## 💡 一句话要点

**提出IAG以解决VLM基础视觉定位系统的后门攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `后门攻击` `多目标攻击` `安全性研究` `视觉定位` `深度学习` `多模态理解`

## 📋 核心要点

1. 当前基于VLM的视觉定位系统在安全性方面存在显著不足，未能有效抵御后门攻击。
2. 本文提出的IAG方法通过动态生成输入感知的触发器，针对特定目标对象进行攻击，具有较高的隐蔽性和有效性。
3. 实验结果表明，IAG在多种设置下的攻击成功率优于现有基线，同时保持了干净样本的准确性和鲁棒性。

## 📝 摘要（中文）

近年来，视觉语言模型（VLMs）的进步显著提升了视觉定位任务的效果。然而，基于VLM的定位系统的安全性尚未得到充分研究。本文揭示了一种新颖且现实的脆弱性：针对VLM基础视觉定位的首个多目标后门攻击。与以往依赖静态触发器或固定目标的攻击不同，我们提出了IAG方法，该方法动态生成输入感知的、文本引导的触发器，基于指定的目标对象描述执行攻击。通过文本条件的UNet，我们将不可察觉的目标语义线索嵌入视觉输入，同时保持对良性样本的正常定位性能。大量实验表明，IAG在多种VLM和基准测试中实现了最佳的攻击成功率，同时不影响干净样本的准确性，保持对现有防御的鲁棒性，并展现出跨数据集和模型的可迁移性。这些发现突显了具备定位能力的VLMs中的安全风险，并强调了对可信多模态理解的进一步研究需求。

## 🔬 方法详解

**问题定义**：本文旨在解决基于VLM的视觉定位系统在面对后门攻击时的脆弱性。现有方法多依赖静态触发器，缺乏针对特定目标的动态适应能力，导致安全性不足。

**核心思路**：IAG方法的核心在于动态生成输入感知的、文本引导的触发器，能够根据目标对象的描述进行调整，从而实现更隐蔽的攻击效果。通过这种设计，攻击者可以在不影响正常样本性能的情况下，成功实施攻击。

**技术框架**：IAG的整体架构包括文本条件的UNet模块，该模块负责将目标语义线索嵌入视觉输入。整个流程分为触发器生成和攻击实施两个主要阶段，确保攻击的隐蔽性和有效性。

**关键创新**：IAG的最重要创新在于其动态生成的触发器能够根据输入的文本描述进行调整，与传统的静态触发器方法本质上不同，提供了更高的灵活性和隐蔽性。

**关键设计**：在技术细节上，IAG采用了联合训练目标，平衡语言能力与感知重建，确保触发器的不可察觉性和攻击的有效性。具体的损失函数设计和网络结构优化也为实现这些目标提供了支持。

## 📊 实验亮点

实验结果显示，IAG在多种VLM（如LLaVA、InternVL、Ferret）和基准测试（如RefCOCO、Flickr30k Entities）中，几乎在所有设置下均实现了最佳的攻击成功率（ASR），同时保持了干净样本的准确性，展现出对现有防御的鲁棒性，具有良好的跨数据集和模型的可迁移性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性敏感的视觉语言系统，如自动驾驶、智能监控和人机交互等。通过识别和缓解后门攻击的风险，可以提升这些系统的安全性和可靠性，确保其在实际应用中的有效性。未来，随着多模态理解的深入发展，该研究将为构建更可信的AI系统提供重要参考。

## 📄 摘要（原文）

> Recent advances in vision-language models (VLMs) have significantly enhanced the visual grounding task, which involves locating objects in an image based on natural language queries. Despite these advancements, the security of VLM-based grounding systems has not been thoroughly investigated. This paper reveals a novel and realistic vulnerability: the first multi-target backdoor attack on VLM-based visual grounding. Unlike prior attacks that rely on static triggers or fixed targets, we propose IAG, a method that dynamically generates input-aware, text-guided triggers conditioned on any specified target object description to execute the attack. This is achieved through a text-conditioned UNet that embeds imperceptible target semantic cues into visual inputs while preserving normal grounding performance on benign samples. We further develop a joint training objective that balances language capability with perceptual reconstruction to ensure imperceptibility, effectiveness, and stealth. Extensive experiments on multiple VLMs (e.g., LLaVA, InternVL, Ferret) and benchmarks (RefCOCO, RefCOCO+, RefCOCOg, Flickr30k Entities, and ShowUI) demonstrate that IAG achieves the best ASRs compared with other baselines on almost all settings without compromising clean accuracy, maintaining robustness against existing defenses, and exhibiting transferability across datasets and models. These findings underscore critical security risks in grounding-capable VLMs and highlight the need for further research on trustworthy multimodal understanding.

