---
layout: default
title: S-Chain: Structured Visual Chain-of-Thought For Medicine
---

# S-Chain: Structured Visual Chain-of-Thought For Medicine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22728" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22728v1</a>
  <a href="https://arxiv.org/pdf/2510.22728.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22728v1" onclick="toggleFavorite(this, '2510.22728v1', 'S-Chain: Structured Visual Chain-of-Thought For Medicine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khai Le-Duc, Duy M. H. Nguyen, Phuong T. H. Trinh, Tien-Phat Nguyen, Nghiem T. Diep, An Ngo, Tung Vu, Trinh Vuong, Anh-Tien Nguyen, Mau Nguyen, Van Trung Hoang, Khai-Nguyen Nguyen, Hy Nguyen, Chris Ngo, Anji Liu, Nhat Ho, Anne-Christin Hauschild, Khanh Xuan Nguyen, Thanh Nguyen-Tang, Pengtao Xie, Daniel Sonntag, James Zou, Mathias Niepert, Anh Totti Nguyen

**分类**: cs.LG, cs.CV

**发布日期**: 2025-10-26

**备注**: First version

---

## 💡 一句话要点

**提出S-Chain数据集，用于提升医学视觉语言模型的可解释性和视觉 grounding 准确性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学视觉问答` `视觉语言模型` `思维链` `视觉 grounding` `数据集构建`

## 📋 核心要点

1. 医学VQA模型缺乏精确的视觉 grounding 和可解释性，限制了其在临床决策中的应用。
2. S-Chain数据集通过专家标注的结构化视觉CoT，将视觉区域与推理步骤显式链接，提升模型推理能力。
3. 实验表明，基于S-Chain训练的模型在可解释性、grounding 保真度和鲁棒性方面均有显著提升。

## 📝 摘要（中文）

医学视觉语言模型（VLMs）中可靠的推理不仅需要准确的预测，还需要文本解释与视觉证据之间的透明对齐。尽管思维链（CoT）提示在医学视觉问答（VQA）中显示出潜力，但尚无大规模专家级数据集捕获具有精确视觉 grounding 的逐步推理。我们推出了S-Chain，这是首个包含12,000张专家标注医学图像的大规模数据集，带有边界框和结构化视觉CoT（SV-CoT），明确地将视觉区域链接到推理步骤。该数据集还支持16种语言，总共超过70万个VQA对，具有广泛的多语言适用性。我们使用S-Chain 对最先进的医学VLMs（ExGra-Med、LLaVA-Med）和通用VLMs（Qwen2.5-VL、InternVL2.5）进行了基准测试，结果表明SV-CoT监督显著提高了可解释性、grounding 保真度和鲁棒性。除了基准测试之外，我们还研究了它与检索增强生成（RAG）的协同作用，揭示了领域知识和视觉 grounding 在自回归推理过程中的相互作用。最后，我们提出了一种新的机制，加强了视觉证据和推理之间的对齐，提高了可靠性和效率。S-Chain 为 grounded 医学推理建立了一个新的基准，并为更值得信赖和可解释的医学VLMs 铺平了道路。

## 🔬 方法详解

**问题定义**：医学视觉问答（VQA）任务旨在根据医学图像回答相关问题。现有的医学VQA模型通常缺乏透明的推理过程和精确的视觉 grounding，难以解释其决策依据，限制了其在临床实践中的应用。现有方法难以将文本推理步骤与图像中的具体区域对应起来，导致模型可能依赖于图像中的无关信息或产生幻觉。

**核心思路**：论文的核心思路是构建一个大规模的、具有结构化视觉思维链（SV-CoT）标注的医学图像数据集S-Chain。通过显式地将图像中的视觉区域与推理步骤联系起来，S-Chain旨在提升医学VQA模型的可解释性、grounding 保真度和鲁棒性。这种结构化的标注方式使得模型能够学习到更加可靠的推理路径，从而做出更准确的预测。

**技术框架**：S-Chain数据集包含12,000张专家标注的医学图像，每张图像都包含边界框和结构化视觉CoT（SV-CoT）标注。SV-CoT标注明确地将视觉区域链接到推理步骤，形成一个推理链。该数据集还支持16种语言，总共超过70万个VQA对。论文还提出了一种新的机制，用于加强视觉证据和推理之间的对齐。该机制的具体实现细节未知。

**关键创新**：S-Chain数据集是首个大规模的、具有专家标注的结构化视觉CoT的医学图像数据集。与以往的数据集相比，S-Chain提供了更丰富的标注信息，能够更有效地指导模型学习。此外，论文还提出了一种新的机制，用于加强视觉证据和推理之间的对齐，进一步提升了模型性能。S-Chain的核心创新在于其结构化的标注方式，它使得模型能够学习到更加可靠的推理路径，从而做出更准确的预测。

**关键设计**：数据集包含12,000张医学图像，并使用专家进行标注，确保标注的质量和准确性。每张图像都包含边界框和结构化视觉CoT（SV-CoT）标注，明确地将视觉区域链接到推理步骤。数据集支持16种语言，以提高模型的泛化能力。论文还研究了S-Chain与检索增强生成（RAG）的协同作用，并提出了一种新的机制来加强视觉证据和推理之间的对齐，但具体的技术细节未详细描述。

## 📊 实验亮点

实验结果表明，使用S-Chain数据集训练的医学VLMs（ExGra-Med、LLaVA-Med）和通用VLMs（Qwen2.5-VL、InternVL2.5）在可解释性、grounding 保真度和鲁棒性方面均有显著提升。具体性能数据和提升幅度未知，但论文强调了SV-CoT监督的有效性。

## 🎯 应用场景

该研究成果可应用于开发更值得信赖和可解释的医学视觉语言模型，辅助医生进行疾病诊断、治疗方案制定等决策。通过提供清晰的推理过程和视觉证据，增强医生对模型的信任度，提高临床决策的效率和准确性。未来可扩展到其他医学影像领域，如病理切片分析等。

## 📄 摘要（原文）

> Faithful reasoning in medical vision-language models (VLMs) requires not only accurate predictions but also transparent alignment between textual rationales and visual evidence. While Chain-of-Thought (CoT) prompting has shown promise in medical visual question answering (VQA), no large-scale expert-level dataset has captured stepwise reasoning with precise visual grounding. We introduce S-Chain, the first large-scale dataset of 12,000 expert-annotated medical images with bounding boxes and structured visual CoT (SV-CoT), explicitly linking visual regions to reasoning steps. The dataset further supports 16 languages, totaling over 700k VQA pairs for broad multilingual applicability. Using S-Chain, we benchmark state-of-the-art medical VLMs (ExGra-Med, LLaVA-Med) and general-purpose VLMs (Qwen2.5-VL, InternVL2.5), showing that SV-CoT supervision significantly improves interpretability, grounding fidelity, and robustness. Beyond benchmarking, we study its synergy with retrieval-augmented generation, revealing how domain knowledge and visual grounding interact during autoregressive reasoning. Finally, we propose a new mechanism that strengthens the alignment between visual evidence and reasoning, improving both reliability and efficiency. S-Chain establishes a new benchmark for grounded medical reasoning and paves the way toward more trustworthy and explainable medical VLMs.

