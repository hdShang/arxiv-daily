---
layout: default
title: "EDVD-LLaMA: Explainable Deepfake Video Detection via Multimodal Large Language Model Reasoning"
---

# EDVD-LLaMA: Explainable Deepfake Video Detection via Multimodal Large Language Model Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16442" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16442v1</a>
  <a href="https://arxiv.org/pdf/2510.16442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16442v1', 'EDVD-LLaMA: Explainable Deepfake Video Detection via Multimodal Large Language Model Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Sun, Chen Cai, Huiping Zhuang, Kong Aik Lee, Lap-Pui Chau, Yi Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-18

---

## 💡 一句话要点

**提出EDVD-LLaMA框架，通过多模态大语言模型推理实现可解释的Deepfake视频检测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Deepfake检测` `多模态大语言模型` `可解释性` `思维链` `时空特征` `面部特征` `视频分析`

## 📋 核心要点

1. 现有Deepfake检测方法缺乏透明性，难以解释检测结果，且泛化能力不足以应对不断演进的伪造技术。
2. 提出EDVD-LLaMA框架，利用多模态大语言模型进行推理，提供可追溯的推理过程和可信的解释，增强检测可解释性。
3. 构建ER-FF++数据集，并设计ST-SIT和Fg-MCoT机制，实验表明EDVD-LLaMA在检测精度、可解释性和鲁棒性方面表现出色。

## 📝 摘要（中文）

深度伪造视频技术的快速发展在促进艺术创作的同时，也使得虚假信息的传播变得更加容易。传统的深度伪造视频检测(DVD)方法面临着原理缺乏透明性以及泛化能力不足以应对不断发展的伪造技术等问题。这突显了对能够识别伪造内容并提供可验证的推理说明的检测器的迫切需求。本文提出了可解释的深度伪造视频检测(EDVD)任务，并设计了EDVD-LLaMA多模态大语言模型(MLLM)推理框架，该框架在提供准确检测结果和可信解释的同时，还提供了可追溯的推理过程。我们的方法首先结合了时空微妙信息Tokenization (ST-SIT)来提取和融合全局和局部跨帧深度伪造特征，为MLLM推理提供丰富的时空语义信息输入。其次，我们构建了一个细粒度的多模态思维链(Fg-MCoT)机制，该机制在推理过程中引入面部特征数据作为硬约束，以实现像素级的时空视频定位，抑制幻觉输出，并提高思维链的可靠性。此外，我们构建了一个可解释推理FF++基准数据集(ER-FF++set)，利用结构化数据来注释视频并确保质量控制，从而支持对推理和检测的双重监督。大量的实验表明，EDVD-LLaMA在检测精度、可解释性以及处理跨伪造方法和跨数据集场景的能力方面都取得了出色的性能和鲁棒性。与之前的DVD方法相比，它提供了一个更可解释和更优越的解决方案。源代码和数据集将公开提供。

## 🔬 方法详解

**问题定义**：论文旨在解决现有Deepfake视频检测方法缺乏可解释性和泛化能力的问题。现有方法通常是黑盒模型，难以理解其决策过程，并且在面对新的伪造技术或跨数据集场景时，性能会显著下降。因此，需要一种能够提供可验证推理过程的、鲁棒性更强的检测方法。

**核心思路**：论文的核心思路是利用多模态大语言模型(MLLM)的推理能力，将Deepfake视频检测转化为一个可解释的推理过程。通过引入时空特征和面部特征作为约束，引导MLLM进行细粒度的分析和判断，从而提高检测的准确性和可信度。这种方法借鉴了人类专家通过观察视频细节并进行逻辑推理来判断真伪的思路。

**技术框架**：EDVD-LLaMA框架主要包含以下几个模块：1) **ST-SIT (Spatio-Temporal Subtle Information Tokenization)**：提取和融合视频中的时空特征，为MLLM提供丰富的语义信息。2) **Fg-MCoT (Fine-grained Multimodal Chain-of-Thought)**：构建细粒度的多模态思维链，利用面部特征作为硬约束，引导MLLM进行推理。3) **MLLM (Large Language Model)**：使用LLaMA作为基础模型，进行多模态输入和推理。整个流程是：输入视频帧，通过ST-SIT提取特征，然后利用Fg-MCoT引导MLLM进行推理，最终输出检测结果和解释。

**关键创新**：论文的关键创新在于将MLLM引入Deepfake视频检测，并设计了ST-SIT和Fg-MCoT机制来增强MLLM的推理能力和可解释性。与传统方法相比，EDVD-LLaMA不仅能够给出检测结果，还能提供可追溯的推理过程，从而提高了检测的可信度。此外，Fg-MCoT机制通过引入面部特征作为硬约束，有效地抑制了MLLM的幻觉输出，提高了推理的可靠性。

**关键设计**：ST-SIT模块的具体实现细节未知，但其目标是提取全局和局部跨帧的Deepfake特征。Fg-MCoT机制的关键在于如何将面部特征有效地融入到MLLM的推理过程中，具体实现细节也未知。ER-FF++数据集的构建使用了结构化数据进行标注，以确保数据质量和支持双重监督。损失函数的设计可能包括检测损失和推理损失，以同时优化检测精度和推理的合理性。

## 📊 实验亮点

EDVD-LLaMA在检测精度、可解释性和鲁棒性方面都取得了显著提升。实验结果表明，该方法在跨伪造方法和跨数据集场景下，依然能够保持较高的检测精度。与之前的DVD方法相比，EDVD-LLaMA提供了一个更可解释和更优越的解决方案，但具体的性能提升数据未知。

## 🎯 应用场景

该研究成果可应用于新闻媒体、社交平台、安全监控等领域，用于检测和识别Deepfake视频，防止虚假信息的传播和恶意攻击。通过提供可解释的检测结果，可以帮助用户更好地理解和信任检测系统，从而提高社会对Deepfake技术的防范意识。

## 📄 摘要（原文）

> The rapid development of deepfake video technology has not only facilitated artistic creation but also made it easier to spread misinformation. Traditional deepfake video detection (DVD) methods face issues such as a lack of transparency in their principles and insufficient generalization capabilities to cope with evolving forgery techniques. This highlights an urgent need for detectors that can identify forged content and provide verifiable reasoning explanations. This paper proposes the explainable deepfake video detection (EDVD) task and designs the EDVD-LLaMA multimodal, a large language model (MLLM) reasoning framework, which provides traceable reasoning processes alongside accurate detection results and trustworthy explanations. Our approach first incorporates a Spatio-Temporal Subtle Information Tokenization (ST-SIT) to extract and fuse global and local cross-frame deepfake features, providing rich spatio-temporal semantic information input for MLLM reasoning. Second, we construct a Fine-grained Multimodal Chain-of-Thought (Fg-MCoT) mechanism, which introduces facial feature data as hard constraints during the reasoning process to achieve pixel-level spatio-temporal video localization, suppress hallucinated outputs, and enhance the reliability of the chain of thought. In addition, we build an Explainable Reasoning FF++ benchmark dataset (ER-FF++set), leveraging structured data to annotate videos and ensure quality control, thereby supporting dual supervision for reasoning and detection. Extensive experiments demonstrate that EDVD-LLaMA achieves outstanding performance and robustness in terms of detection accuracy, explainability, and its ability to handle cross-forgery methods and cross-dataset scenarios. Compared to previous DVD methods, it provides a more explainable and superior solution. The source code and dataset will be publicly available.

