---
layout: default
title: "EyePCR: A Comprehensive Benchmark for Fine-Grained Perception, Knowledge Comprehension and Clinical Reasoning in Ophthalmic Surgery"
---

# EyePCR: A Comprehensive Benchmark for Fine-Grained Perception, Knowledge Comprehension and Clinical Reasoning in Ophthalmic Surgery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15596" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15596v2</a>
  <a href="https://arxiv.org/pdf/2509.15596.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15596v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15596v2', 'EyePCR: A Comprehensive Benchmark for Fine-Grained Perception, Knowledge Comprehension and Clinical Reasoning in Ophthalmic Surgery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gui Wang, Yang Wennuo, Xusen Ma, Zehao Zhong, Zhuoru Wu, Ende Wu, Rong Qu, Wooi Ping Cheah, Jianfeng Ren, Linlin Shen

**分类**: cs.CV

**发布日期**: 2025-09-19 (更新: 2025-10-02)

**备注**: Strong accept by NeurIPS2025 Reviewers and AC

---

## 💡 一句话要点

**EyePCR：眼科手术中细粒度感知、知识理解和临床推理的综合基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `眼科手术` `多模态大语言模型` `基准数据集` `临床推理` `医学知识图谱` `视觉问答` `领域自适应`

## 📋 核心要点

1. 现有MLLM在眼科手术等高风险领域表现不足，缺乏针对性的评估基准。
2. EyePCR构建大规模眼科手术基准，包含感知、理解和推理三个认知维度，并提供丰富的标注。
3. EyePCR-MLLM在感知任务上取得最高准确率，并在理解和推理上超越开源模型，接近商业模型水平。

## 📝 摘要（中文）

多模态大型语言模型(MLLMs)已经展示了卓越的能力，但它们在高风险、特定领域的场景（如手术环境）中的性能在很大程度上仍未被探索。为了解决这一差距，我们开发了EyePCR，这是一个用于眼科手术分析的大规模基准，它基于结构化的临床知识来评估跨感知、理解和推理的认知能力。EyePCR提供了一个丰富注释的语料库，包含超过21万个VQAs，涵盖1048个用于多视角感知的细粒度属性，一个包含超过2.5万个三元组的医学知识图谱用于理解，以及四个临床基础的推理任务。丰富的注释有助于深入的认知分析，模拟外科医生如何感知视觉线索并将它们与领域知识相结合以做出决策，从而大大提高模型的认知能力。特别是，EyePCR-MLLM，Qwen2.5-VL-7B的领域自适应变体，在感知的多项选择题中实现了最高的准确率，并在理解和推理方面优于开源模型，与GPT-4.1等商业模型相媲美。EyePCR揭示了现有MLLM在手术认知方面的局限性，并为基准测试和提高手术视频理解模型的临床可靠性奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLMs）在眼科手术这一高风险、专业领域中认知能力不足的问题。现有方法缺乏针对手术场景的细粒度评估基准，无法有效衡量模型在感知、理解和推理方面的能力，阻碍了模型在该领域的应用。

**核心思路**：论文的核心思路是构建一个大规模、高质量的眼科手术基准数据集EyePCR，该数据集包含丰富的标注信息，涵盖感知、理解和推理三个认知维度。通过在该基准上评估MLLMs的性能，可以深入了解模型在手术场景中的局限性，并为模型在该领域的改进提供指导。

**技术框架**：EyePCR基准数据集包含以下几个主要组成部分：1) 超过21万个视觉问答对（VQAs），涵盖1048个细粒度属性，用于评估模型的感知能力；2) 一个包含超过2.5万个三元组的医学知识图谱，用于评估模型的理解能力；3) 四个临床基础的推理任务，用于评估模型的推理能力。此外，论文还提出了一个领域自适应的MLLM模型EyePCR-MLLM，该模型基于Qwen2.5-VL-7B进行微调。

**关键创新**：EyePCR的主要创新点在于其构建了一个大规模、高质量的眼科手术基准数据集，该数据集不仅包含丰富的标注信息，而且涵盖了感知、理解和推理三个认知维度。此外，论文还提出了一个领域自适应的MLLM模型EyePCR-MLLM，该模型在EyePCR基准上取得了显著的性能提升。

**关键设计**：EyePCR数据集的构建过程中，作者精心设计了VQAs、知识图谱和推理任务，以确保数据集能够全面、准确地评估MLLMs在眼科手术场景中的认知能力。EyePCR-MLLM模型则采用了领域自适应的微调策略，利用EyePCR数据集对Qwen2.5-VL-7B模型进行微调，从而使其更好地适应眼科手术场景。

## 📊 实验亮点

EyePCR-MLLM在EyePCR基准的感知任务中，多项选择题的准确率达到了最高水平，超过了其他对比模型。在理解和推理任务中，EyePCR-MLLM也优于开源模型，并且性能接近GPT-4.1等商业模型，证明了领域自适应微调的有效性以及EyePCR基准的价值。

## 🎯 应用场景

该研究成果可应用于开发智能手术辅助系统，帮助医生进行术前规划、术中导航和术后评估。通过提升模型在眼科手术领域的感知、理解和推理能力，可以提高手术的安全性、效率和准确性，最终改善患者的治疗效果。未来，该基准和模型可以推广到其他医学领域，促进医疗人工智能的发展。

## 📄 摘要（原文）

> MLLMs (Multimodal Large Language Models) have showcased remarkable capabilities, but their performance in high-stakes, domain-specific scenarios like surgical settings, remains largely under-explored. To address this gap, we develop \textbf{EyePCR}, a large-scale benchmark for ophthalmic surgery analysis, grounded in structured clinical knowledge to evaluate cognition across \textit{Perception}, \textit{Comprehension} and \textit{Reasoning}. EyePCR offers a richly annotated corpus with more than 210k VQAs, which cover 1048 fine-grained attributes for multi-view perception, medical knowledge graph of more than 25k triplets for comprehension, and four clinically grounded reasoning tasks. The rich annotations facilitate in-depth cognitive analysis, simulating how surgeons perceive visual cues and combine them with domain knowledge to make decisions, thus greatly improving models' cognitive ability. In particular, \textbf{EyePCR-MLLM}, a domain-adapted variant of Qwen2.5-VL-7B, achieves the highest accuracy on MCQs for \textit{Perception} among compared models and outperforms open-source models in \textit{Comprehension} and \textit{Reasoning}, rivalling commercial models like GPT-4.1. EyePCR reveals the limitations of existing MLLMs in surgical cognition and lays the foundation for benchmarking and enhancing clinical reliability of surgical video understanding models.

