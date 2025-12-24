---
layout: default
title: PMF-CEC: Phoneme-augmented Multimodal Fusion for Context-aware ASR Error Correction with Error-specific Selective Decoding
---

# PMF-CEC: Phoneme-augmented Multimodal Fusion for Context-aware ASR Error Correction with Error-specific Selective Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11064" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11064v1</a>
  <a href="https://arxiv.org/pdf/2506.11064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11064v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11064v1', 'PMF-CEC: Phoneme-augmented Multimodal Fusion for Context-aware ASR Error Correction with Error-specific Selective Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun He, Tomoki Toda

**分类**: eess.AS, cs.AI, cs.CL, cs.SD

**发布日期**: 2025-05-31

**备注**: Accepted by IEEE TASLP 2025

---

## 💡 一句话要点

**提出PMF-CEC以解决ASR错误纠正中的同音词问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动语音识别` `错误纠正` `多模态融合` `音素增强` `上下文感知` `深度学习` `同音词处理`

## 📋 核心要点

1. 现有的ASR后处理方法在处理发音相似的稀有词时准确性不足，导致错误纠正效果不理想。
2. 论文提出的PMF-CEC方法通过音素增强和多模态融合，改善了对同音词的区分能力，从而提高了错误纠正的准确性。
3. 实验结果显示，PMF-CEC在多个数据集上相较于ED-CEC显著降低了偏差词错误率，并在推理速度和鲁棒性上优于其他方法。

## 📝 摘要（中文）

端到端的自动语音识别（ASR）模型在准确识别稀有词方面常常面临挑战。我们之前提出的错误检测和上下文感知错误纠正（ED-CEC）方法利用上下文信息来提高ASR转录的准确性。尽管ED-CEC在纠正稀有词方面取得了一定成功，但在处理发音相似但拼写不同的稀有词时，其准确性仍然较低。为了解决这一问题，我们提出了一种基于ED-CEC的音素增强多模态融合方法（PMF-CEC），使得目标稀有词和同音词之间的区分更加明确。此外，我们还引入了保留概率机制，以过滤掉置信度低于设定阈值的编辑操作，从而提高错误检测的准确性。实验结果表明，PMF-CEC在保持合理推理速度的同时，进一步降低了偏差词错误率，尤其在纠正同音词方面表现出更强的优势。

## 🔬 方法详解

**问题定义**：本论文旨在解决ASR模型在识别发音相似但拼写不同的稀有词时的低准确性问题。现有的ED-CEC方法在此方面表现不佳，尤其是在同音词的纠正上存在明显不足。

**核心思路**：PMF-CEC方法通过引入音素信息和多模态融合技术，增强了对稀有词的区分能力，特别是在处理同音词时，能够更有效地进行错误纠正。

**技术框架**：PMF-CEC的整体架构包括音素增强模块、上下文感知错误检测模块和保留概率机制。音素增强模块负责提取音素特征，上下文感知模块利用上下文信息进行错误检测，而保留概率机制则用于过滤低置信度的编辑操作。

**关键创新**：PMF-CEC的主要创新在于音素增强与多模态融合的结合，显著提高了对同音词的区分能力，克服了ED-CEC在处理相似发音词时的局限性。

**关键设计**：在设计中，保留概率机制的阈值设置是关键参数，通过调整该阈值，可以有效提高错误检测的准确性。此外，网络结构采用了深度学习模型，以适应多模态输入的特征提取。

## 📊 实验亮点

实验结果表明，PMF-CEC在五个数据集上相较于ED-CEC显著降低了偏差词错误率，尤其在纠正同音词方面表现出更强的优势。此外，PMF-CEC在推理速度上保持合理，优于其他上下文偏置方法，显示出更好的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括语音助手、自动字幕生成和电话客服系统等，能够显著提高这些系统在处理复杂语言环境下的准确性和用户体验。未来，随着技术的不断发展，PMF-CEC方法有望在更多实际应用中发挥重要作用，尤其是在多语种和方言识别方面。

## 📄 摘要（原文）

> End-to-end automatic speech recognition (ASR) models often struggle to accurately recognize rare words. Previously, we introduced an ASR postprocessing method called error detection and context-aware error correction (ED-CEC), which leverages contextual information such as named entities and technical terms to improve the accuracy of ASR transcripts. Although ED-CEC achieves a notable success in correcting rare words, its accuracy remains low when dealing with rare words that have similar pronunciations but different spellings. To address this issue, we proposed a phoneme-augmented multimodal fusion method for context-aware error correction (PMF-CEC) method on the basis of ED-CEC, which allowed for better differentiation between target rare words and homophones. Additionally, we observed that the previous ASR error detection module suffers from overdetection. To mitigate this, we introduced a retention probability mechanism to filter out editing operations with confidence scores below a set threshold, preserving the original operation to improve error detection accuracy. Experiments conducted on five datasets demonstrated that our proposed PMF-CEC maintains reasonable inference speed while further reducing the biased word error rate compared with ED-CEC, showing a stronger advantage in correcting homophones. Moreover, our method outperforms other contextual biasing methods, and remains valuable compared with LLM-based methods in terms of faster inference and better robustness under large biasing lists.

