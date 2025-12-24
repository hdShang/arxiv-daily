---
layout: default
title: MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios
---

# MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21333" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21333v2</a>
  <a href="https://arxiv.org/pdf/2505.21333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21333v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21333v2', 'MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Shi, Huanqian Wang, Wulin Xie, Huanyao Zhang, Lijie Zhao, Yi-Fan Zhang, Xinfeng Li, Chaoyou Fu, Zhuoer Wen, Wenting Liu, Zhuoran Zhang, Xinlong Chen, Bohan Zeng, Sihan Yang, Yushuo Guan, Zhang Zhang, Liang Wang, Haoxuan Li, Zhouchen Lin, Yuanxing Zhang, Pengfei Wan, Haotian Wang, Wenjing Yang

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-09-25)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出MME-VideoOCR以解决视频场景下OCR效果不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频OCR` `多模态大语言模型` `时空推理` `动态视频理解` `基准评估`

## 📋 核心要点

1. 现有的多模态大语言模型在视频OCR中表现不佳，尤其是在处理动态视频场景时，面临运动模糊和时间变化等挑战。
2. 论文提出MME-VideoOCR基准，涵盖多种视频OCR任务，旨在评估和提升多模态大语言模型在视频理解中的能力。
3. 实验结果表明，现有模型在单帧文本识别任务上表现良好，但在需要整体视频理解的任务上能力有限，尤其是在时空推理方面。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在静态图像的光学字符识别（OCR）方面取得了显著准确性。然而，由于运动模糊、时间变化和视频内容固有的视觉效果，其在视频OCR中的有效性显著降低。为提供更清晰的训练指导，本文引入了MME-VideoOCR基准，涵盖了广泛的视频OCR应用场景。该基准包含10个任务类别、25个独立任务和44种不同场景，任务不仅限于文本识别，还包括对视频中文本内容的深入理解和推理。基准由1464个不同分辨率、长宽比和时长的视频以及2000个精心策划的手动标注问答对组成。对18个最先进的MLLMs进行评估，结果显示即使是表现最佳的模型（Gemini-2.5 Pro）准确率也仅为73.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大语言模型在视频OCR任务中的有效性不足，尤其是在动态场景中面临的挑战，如运动模糊和时间变化。

**核心思路**：通过引入MME-VideoOCR基准，提供多样化的任务和场景，以促进模型在视频理解和文本推理方面的能力提升。

**技术框架**：MME-VideoOCR基准包括10个任务类别和25个独立任务，涵盖了从文本识别到深层理解的多个阶段，整体架构设计旨在评估模型在不同视频场景下的表现。

**关键创新**：最重要的创新点在于构建了一个全面的基准，包含多种视频OCR任务和丰富的场景设置，填补了现有研究在动态视频OCR评估方面的空白。

**关键设计**：基准包含1464个视频样本和2000个手动标注的问答对，确保了数据的多样性和准确性，为模型训练和评估提供了坚实基础。

## 📊 实验亮点

实验结果显示，最佳模型Gemini-2.5 Pro在MME-VideoOCR基准上的准确率仅为73.7%，表明现有模型在处理复杂视频理解任务时的局限性，尤其是在需要时空推理和跨帧信息整合的场景中表现不佳。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动字幕生成、教育视频分析等，能够为多模态大语言模型在视频理解方面的实际应用提供指导和支持。未来，随着技术的进步，MME-VideoOCR基准将推动视频OCR技术的进一步发展，提升其在实际场景中的应用价值。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved considerable accuracy in Optical Character Recognition (OCR) from static images. However, their efficacy in video OCR is significantly diminished due to factors such as motion blur, temporal variations, and visual effects inherent in video content. To provide clearer guidance for training practical MLLMs, we introduce the MME-VideoOCR benchmark, which encompasses a comprehensive range of video OCR application scenarios. MME-VideoOCR features 10 task categories comprising 25 individual tasks and spans 44 diverse scenarios. These tasks extend beyond text recognition to incorporate deeper comprehension and reasoning of textual content within videos. The benchmark consists of 1,464 videos with varying resolutions, aspect ratios, and durations, along with 2,000 meticulously curated, manually annotated question-answer pairs. We evaluate 18 state-of-the-art MLLMs on MME-VideoOCR, revealing that even the best-performing model (Gemini-2.5 Pro) achieves an accuracy of only 73.7%. Fine-grained analysis indicates that while existing MLLMs demonstrate strong performance on tasks where relevant texts are contained within a single or few frames, they exhibit limited capability in effectively handling tasks that demand holistic video comprehension. These limitations are especially evident in scenarios that require spatio-temporal reasoning, cross-frame information integration, or resistance to language prior bias. Our findings also highlight the importance of high-resolution visual input and sufficient temporal coverage for reliable OCR in dynamic video scenarios.

