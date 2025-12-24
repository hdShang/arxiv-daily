---
layout: default
title: "HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs"
---

# HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00088" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00088v1</a>
  <a href="https://arxiv.org/pdf/2506.00088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00088v1', 'HD-NDEs: Neural Differential Equations for Hallucination Detection in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qing Li, Jiahui Geng, Zongxiong Chen, Derui Zhu, Yuxia Wang, Congbo Ma, Chenyang Lyu, Fakhri Karray

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出HD-NDEs以解决大语言模型中的幻觉检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幻觉检测` `神经微分方程` `大型语言模型` `动态建模` `真实性评估` `自然语言处理` `信息检索`

## 📋 核心要点

1. 现有方法在处理输出序列早期或中期的非事实信息时，可靠性不足，导致幻觉现象难以有效检测。
2. 本文提出HD-NDEs，通过神经微分方程建模LLMs潜在空间的动态系统，从而系统性地评估陈述的真实性。
3. 在五个数据集和六个LLMs上的实验结果显示，HD-NDEs在True-False数据集上AUC-ROC提升超过14%，验证了其有效性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）取得了显著进展，但幻觉现象，即模型生成不准确或非事实陈述，仍然是实际应用中的重大挑战。尽管现有的基于分类的方法（如SAPLMA）在减轻幻觉方面效率较高，但在输出序列的早期或中期出现非事实信息时，它们的可靠性受到影响。为了解决这些问题，本文提出了幻觉检测-神经微分方程（HD-NDEs），这是一种新颖的方法，通过捕捉LLMs潜在空间中的动态系统，系统性地评估陈述的真实性。我们的实验在五个数据集和六个广泛使用的LLMs上进行了广泛测试，结果表明HD-NDEs的有效性，尤其是在True-False数据集上相比于最先进的技术，AUC-ROC提升超过14%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中幻觉现象的检测问题。现有的分类方法在处理输出序列早期或中期的非事实信息时，表现出较低的可靠性，导致幻觉现象难以有效识别。

**核心思路**：HD-NDEs通过应用神经微分方程，建模LLMs潜在空间中的动态系统，从而系统性地评估生成陈述的真实性。这种方法能够捕捉到模型生成过程中的动态变化，提供更准确的判断依据。

**技术框架**：HD-NDEs的整体架构包括两个主要模块：首先，利用神经微分方程建模LLMs的潜在空间动态；其次，将潜在空间中的序列映射到分类空间进行真实性评估。

**关键创新**：HD-NDEs的核心创新在于将神经微分方程引入幻觉检测领域，能够全面捕捉LLMs生成过程中的动态特征，与传统的静态分类方法相比，提供了更深层次的理解和评估。

**关键设计**：在设计中，HD-NDEs采用了特定的损失函数以优化模型的真实性评估能力，并在网络结构上进行了调整，以适应潜在空间的动态建模需求。

## 📊 实验亮点

实验结果显示，HD-NDEs在True-False数据集上的AUC-ROC提升超过14%，显著优于现有的最先进技术。这一提升表明HD-NDEs在幻觉检测方面的有效性，尤其是在处理早期或中期输出时的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过提高幻觉检测的准确性，HD-NDEs能够增强大型语言模型在实际应用中的可靠性，进而推动智能助手、自动问答系统等技术的发展。未来，该方法可能会影响更广泛的AI应用，提升人机交互的质量。

## 📄 摘要（原文）

> In recent years, large language models (LLMs) have made remarkable advancements, yet hallucination, where models produce inaccurate or non-factual statements, remains a significant challenge for real-world deployment. Although current classification-based methods, such as SAPLMA, are highly efficient in mitigating hallucinations, they struggle when non-factual information arises in the early or mid-sequence of outputs, reducing their reliability. To address these issues, we propose Hallucination Detection-Neural Differential Equations (HD-NDEs), a novel method that systematically assesses the truthfulness of statements by capturing the full dynamics of LLMs within their latent space. Our approaches apply neural differential equations (Neural DEs) to model the dynamic system in the latent space of LLMs. Then, the sequence in the latent space is mapped to the classification space for truth assessment. The extensive experiments across five datasets and six widely used LLMs demonstrate the effectiveness of HD-NDEs, especially, achieving over 14% improvement in AUC-ROC on the True-False dataset compared to state-of-the-art techniques.

