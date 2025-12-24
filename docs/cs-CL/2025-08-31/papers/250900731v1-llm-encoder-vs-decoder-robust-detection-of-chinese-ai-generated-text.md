---
layout: default
title: "LLM Encoder vs. Decoder: Robust Detection of Chinese AI-Generated Text with LoRA"
---

# LLM Encoder vs. Decoder: Robust Detection of Chinese AI-Generated Text with LoRA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00731" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00731v1</a>
  <a href="https://arxiv.org/pdf/2509.00731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00731v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00731v1', 'LLM Encoder vs. Decoder: Robust Detection of Chinese AI-Generated Text with LoRA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Houji Jin, Negin Ashrafi, Armin Abdollahi, Wei Liu, Jian Wang, Ganyu Gui, Maryam Pishgar, Huanghao Feng

**分类**: cs.CL

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出基于LoRA的解码器模型以提高中文AI生成文本检测的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `中文文本检测` `AI生成文本` `解码器模型` `LoRA` `鲁棒性` `深度学习` `模型微调`

## 📋 核心要点

1. 现有的中文AI生成文本检测方法在面对语言细微差异时表现不佳，尤其是编码器模型在分布变化下性能显著下降。
2. 本研究提出了一种基于LoRA的解码器模型，通过轻量级分类头和指令格式输入进行适配，提升了模型的检测能力。
3. 实验结果显示，LoRA适配的Qwen2.5-7B模型在测试集上达到了95.94%的准确率，显著高于其他基线模型，展现了更好的鲁棒性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，准确检测AI生成文本的需求日益增加，尤其是在中文等语言中，细微的语言差异对现有方法构成了重大挑战。本研究系统比较了基于编码器的Transformer模型（如中文BERT-large和RoBERTa-wwm-ext-large）、仅解码的LLM（阿里巴巴的Qwen2.5-7B）以及使用NLPCC 2025中文AI生成文本检测任务的FastText基线。实验结果表明，尽管编码器模型几乎记住了训练数据，但在分布变化下性能显著下降。相较之下，LoRA适配的Qwen2.5-7B在测试中达到了95.94%的准确率，显示出优越的泛化能力和对数据集特定伪影的抵抗力。

## 🔬 方法详解

**问题定义**：本研究旨在解决中文AI生成文本检测中的鲁棒性问题，现有的编码器模型在面对数据分布变化时表现不佳，导致准确率下降。

**核心思路**：论文提出使用解码器模型Qwen2.5-7B，并通过LoRA进行参数高效的微调，以提高模型在不同数据集上的泛化能力。

**技术框架**：整体架构包括数据预处理、模型适配和分类阶段。编码器模型通过新颖的基于提示的掩码语言建模进行微调，而解码器模型则采用指令格式输入和轻量级分类头。

**关键创新**：最重要的创新在于使用LoRA对解码器模型进行微调，使其在保持高性能的同时，显著提高了对数据集特定伪影的抵抗力，与传统的编码器模型形成鲜明对比。

**关键设计**：在模型设计中，采用了轻量级分类头，并通过LoRA进行参数适配，确保了模型在训练过程中的高效性和准确性。

## 📊 实验亮点

实验结果显示，LoRA适配的Qwen2.5-7B模型在测试集上达到了95.94%的准确率，平衡的精确率和召回率指标表明其在鲁棒性和泛化能力上优于编码器模型（BERT: 79.3%，RoBERTa: 76.3%）和FastText（83.5%）。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、教育领域的文本生成检测以及新闻报道的真实性验证等。通过提高中文AI生成文本的检测能力，可以有效防止虚假信息的传播，提升信息的可信度和安全性。

## 📄 摘要（原文）

> The rapid growth of large language models (LLMs) has heightened the demand for accurate detection of AI-generated text, particularly in languages like Chinese, where subtle linguistic nuances pose significant challenges to current methods. In this study, we conduct a systematic comparison of encoder-based Transformers (Chinese BERT-large and RoBERTa-wwm-ext-large), a decoder-only LLM (Alibaba's Qwen2.5-7B/DeepSeek-R1-Distill-Qwen-7B fine-tuned via Low-Rank Adaptation, LoRA), and a FastText baseline using the publicly available dataset from the NLPCC 2025 Chinese AI-Generated Text Detection Task. Encoder models were fine-tuned using a novel prompt-based masked language modeling approach, while Qwen2.5-7B was adapted for classification with an instruction-format input and a lightweight classification head trained via LoRA. Experiments reveal that although encoder models nearly memorize training data, they suffer significant performance degradation under distribution shifts (RoBERTa: 76.3% test accuracy; BERT: 79.3%). FastText demonstrates surprising lexical robustness (83.5% accuracy) yet lacks deeper semantic understanding. In contrast, the LoRA-adapted Qwen2.5-7B achieves 95.94% test accuracy with balanced precision-recall metrics, indicating superior generalization and resilience to dataset-specific artifacts. These findings underscore the efficacy of decoder-based LLMs with parameter-efficient fine-tuning for robust Chinese AI-generated text detection. Future work will explore next-generation Qwen3 models, distilled variants, and ensemble strategies to enhance cross-domain robustness further.

