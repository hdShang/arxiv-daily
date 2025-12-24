---
layout: default
title: "Bridging Human Oversight and Black-box Driver Assistance: Vision-Language Models for Predictive Alerting in Lane Keeping Assist Systems"
---

# Bridging Human Oversight and Black-box Driver Assistance: Vision-Language Models for Predictive Alerting in Lane Keeping Assist Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11535" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11535v1</a>
  <a href="https://arxiv.org/pdf/2505.11535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11535v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11535v1', 'Bridging Human Oversight and Black-box Driver Assistance: Vision-Language Models for Predictive Alerting in Lane Keeping Assist Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhang Wang, Hao Zhou

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-05-14

---

## 💡 一句话要点

**提出LKAlert以解决LKA系统人机协作不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `车道保持辅助` `视觉-语言模型` `可解释人工智能` `多模态融合` `实时预测` `自动驾驶系统` `人机协作`

## 📋 核心要点

1. 现有的LKA系统由于其黑箱特性，导致驾驶员难以预判系统行为，从而影响信任和安全性。
2. LKAlert通过结合视觉-语言模型，提前预测LKA风险，并提供自然语言解释，增强驾驶员的情境意识。
3. 实验结果显示，LKAlert在预测LKA故障方面取得了69.8%的准确率和58.6%的F1-score，且生成的文本解释质量高，适合实时应用。

## 📝 摘要（中文）

车道保持辅助系统（LKA）在实际应用中常面临不可预测的故障，主要源于其黑箱特性，限制了驾驶员的预判和信任。为此，本文提出了LKAlert，一个新型的监督警报系统，利用视觉-语言模型（VLM）提前1-3秒预测潜在的LKA风险。LKAlert处理行车记录仪视频和CAN数据，并结合可解释模型的替代车道分割特征，提供自动化的引导注意力。与传统的二元分类器不同，LKAlert不仅发出预测警报，还提供简洁的自然语言解释，增强驾驶员的情境意识和信任。我们还引入了OpenLKA-Alert，这是第一个为预测和可解释LKA故障警告设计的基准数据集，包含同步的多模态输入和人工撰写的解释。实验证明，该系统以69.8%的准确率和58.6%的F1-score成功预测即将发生的LKA故障，并生成高质量的文本解释，适合实时车载使用。

## 🔬 方法详解

**问题定义**：本文旨在解决车道保持辅助系统（LKA）在实际应用中由于黑箱特性导致的不可预测故障问题，影响驾驶员的信任和安全性。

**核心思路**：LKAlert通过视觉-语言模型（VLM）结合多模态数据，提前预测LKA风险，并提供自然语言解释，以增强驾驶员的情境意识和信任。

**技术框架**：LKAlert的整体架构包括数据输入模块（行车记录仪视频和CAN数据）、特征提取模块（替代车道分割特征）、预测模块（基于VLM的风险预测）和解释模块（生成自然语言解释）。

**关键创新**：LKAlert的创新之处在于其结合了可解释模型的特征引导与VLM的推理能力，能够在不改变视觉主干的情况下，进行结构化视觉上下文的推理，适用于其他复杂的黑箱系统。

**关键设计**：在模型设计中，采用了LoRA技术以优化模型参数，确保在保持高效性的同时，能够生成高质量的文本解释，此外，系统运行频率约为2 Hz，适合实时应用。

## 📊 实验亮点

实验结果表明，LKAlert在预测即将发生的LKA故障方面达到了69.8%的准确率和58.6%的F1-score，生成的文本解释质量高（71.7 ROUGE-L），且系统运行效率为约2 Hz，证明了其在实时车载应用中的可行性。

## 🎯 应用场景

LKAlert的研究成果在自动驾驶辅助系统（ADAS）中具有广泛的应用潜力，能够提升驾驶员对系统的信任和安全感。通过提供可解释的预测警报，该系统可用于各种需要人机协作的场景，未来可能推动更安全的自动驾驶技术发展。

## 📄 摘要（原文）

> Lane Keeping Assist systems, while increasingly prevalent, often suffer from unpredictable real-world failures, largely due to their opaque, black-box nature, which limits driver anticipation and trust. To bridge the gap between automated assistance and effective human oversight, we present LKAlert, a novel supervisory alert system that leverages VLM to forecast potential LKA risk 1-3 seconds in advance. LKAlert processes dash-cam video and CAN data, integrating surrogate lane segmentation features from a parallel interpretable model as automated guiding attention. Unlike traditional binary classifiers, LKAlert issues both predictive alert and concise natural language explanation, enhancing driver situational awareness and trust. To support the development and evaluation of such systems, we introduce OpenLKA-Alert, the first benchmark dataset designed for predictive and explainable LKA failure warnings. It contains synchronized multimodal inputs and human-authored justifications across annotated temporal windows. We further contribute a generalizable methodological framework for VLM-based black-box behavior prediction, combining surrogate feature guidance with LoRA. This framework enables VLM to reason over structured visual context without altering its vision backbone, making it broadly applicable to other complex, opaque systems requiring interpretable oversight. Empirical results correctly predicts upcoming LKA failures with 69.8% accuracy and a 58.6\% F1-score. The system also generates high-quality textual explanations for drivers (71.7 ROUGE-L) and operates efficiently at approximately 2 Hz, confirming its suitability for real-time, in-vehicle use. Our findings establish LKAlert as a practical solution for enhancing the safety and usability of current ADAS and offer a scalable paradigm for applying VLMs to human-centered supervision of black-box automation.

