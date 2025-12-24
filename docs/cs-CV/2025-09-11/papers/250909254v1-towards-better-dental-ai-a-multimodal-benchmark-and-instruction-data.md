---
layout: default
title: "Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis"
---

# Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09254" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09254v1</a>
  <a href="https://arxiv.org/pdf/2509.09254.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09254v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09254v1', 'Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Hao, Yuxuan Fan, Yanpeng Sun, Kaixin Guo, Lizhuo Lin, Jinrong Yang, Qi Yong H. Ai, Lun M. Wong, Hao Tang, Kuo Feng Hung

**分类**: cs.CV, cs.MM

**发布日期**: 2025-09-11

**备注**: 40 pages, 26 figures, 9 tables

**🔗 代码/项目**: [GITHUB](https://github.com/isbrycee/OralGPT)

---

## 💡 一句话要点

**提出MMOral：用于全景X光分析的多模态基准和指令数据集，并构建OralGPT模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `指令学习` `牙科影像分析` `全景X光片` `大型视觉语言模型`

## 📋 核心要点

1. 现有医学基准和指令数据集难以捕捉全景X光片中密集的解剖结构和细微的病理线索，限制了大型视觉语言模型在牙科领域的应用。
2. 论文构建了大规模多模态指令数据集MMOral，并提出了OralGPT模型，通过监督微调提升模型在全景X光片分析任务上的性能。
3. 实验结果表明，即使是GPT-4o在MMOral-Bench上的准确率也较低，而OralGPT通过单轮监督微调即可获得显著的性能提升。

## 📝 摘要（中文）

本文提出MMOral，首个专为全景X光片解读设计的大规模多模态指令数据集和基准。MMOral包含20563张带注释的图像，以及130万个指令遵循实例，涵盖属性提取、报告生成、视觉问答和图像引导对话等多种任务类型。此外，论文还提出了MMOral-Bench，一个包含牙科五个关键诊断维度的综合评估套件。在MMOral-Bench上评估了64个大型视觉语言模型（LVLM），结果表明，即使是表现最佳的模型GPT-4o也仅达到41.45%的准确率，揭示了当前模型在该领域的局限性。为了促进该领域的进展，论文还提出了OralGPT，通过在Qwen2.5-VL-7B上使用精心策划的MMOral指令数据集进行监督微调（SFT）。值得注意的是，单轮SFT即可显著提升LVLM的性能，例如OralGPT的性能提升了24.73%。MMOral和OralGPT都具有作为智能牙科关键基础的巨大潜力，并能够在该领域实现更具临床影响力的多模态AI系统。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大型视觉语言模型（LVLM）在牙科全景X光片分析方面表现不足的问题。现有的医学基准数据集和指令数据集无法充分捕捉全景X光片中复杂的解剖结构和细微的病理特征，导致LVLM难以在该领域取得良好的性能。因此，需要一个专门为牙科全景X光片分析设计的大规模多模态数据集和评估基准。

**核心思路**：论文的核心思路是构建一个高质量、大规模的多模态指令数据集MMOral，并利用该数据集对LVLM进行监督微调，从而提升模型在牙科全景X光片分析任务上的性能。通过指令学习的方式，使模型能够更好地理解和执行各种牙科相关的任务，例如属性提取、报告生成、视觉问答和图像引导对话。

**技术框架**：整体框架包含两个主要部分：MMOral数据集的构建和OralGPT模型的训练。MMOral数据集的构建涉及图像收集、标注和指令生成等步骤。OralGPT模型的训练则是在预训练的LVLM（Qwen2.5-VL-7B）的基础上，使用MMOral数据集进行监督微调（SFT）。此外，论文还提出了MMOral-Bench，用于评估模型在牙科领域的性能。

**关键创新**：论文的关键创新在于构建了首个专为牙科全景X光片分析设计的大规模多模态指令数据集MMOral。该数据集包含了丰富的标注信息和多样化的指令，能够有效地提升LVLM在该领域的性能。此外，论文还提出了OralGPT模型，通过监督微调的方式，显著提升了LVLM在全景X光片分析任务上的准确率。

**关键设计**：MMOral数据集包含20,563张带注释的图像和130万个指令遵循实例，涵盖属性提取、报告生成、视觉问答和图像引导对话等多种任务类型。OralGPT模型使用Qwen2.5-VL-7B作为基础模型，并使用MMOral数据集进行单轮监督微调。MMOral-Bench包含牙科五个关键诊断维度，用于全面评估模型在牙科领域的性能。

## 📊 实验亮点

实验结果表明，即使是表现最佳的GPT-4o模型在MMOral-Bench上的准确率仅为41.45%，表明现有模型在牙科领域的局限性。通过在Qwen2.5-VL-7B上使用MMOral数据集进行单轮监督微调，OralGPT模型的性能提升了24.73%，证明了MMOral数据集和监督微调方法的有效性。

## 🎯 应用场景

该研究成果可应用于智能牙科领域，例如辅助牙医进行诊断、生成诊断报告、回答患者提问等。通过提升LVLM在牙科全景X光片分析方面的能力，可以提高诊断效率和准确性，改善患者的就医体验，并为远程医疗提供技术支持。未来，该研究还可以扩展到其他医学影像领域，为构建更智能的医疗AI系统奠定基础。

## 📄 摘要（原文）

> Recent advances in large vision-language models (LVLMs) have demonstrated strong performance on general-purpose medical tasks. However, their effectiveness in specialized domains such as dentistry remains underexplored. In particular, panoramic X-rays, a widely used imaging modality in oral radiology, pose interpretative challenges due to dense anatomical structures and subtle pathological cues, which are not captured by existing medical benchmarks or instruction datasets. To this end, we introduce MMOral, the first large-scale multimodal instruction dataset and benchmark tailored for panoramic X-ray interpretation. MMOral consists of 20,563 annotated images paired with 1.3 million instruction-following instances across diverse task types, including attribute extraction, report generation, visual question answering, and image-grounded dialogue. In addition, we present MMOral-Bench, a comprehensive evaluation suite covering five key diagnostic dimensions in dentistry. We evaluate 64 LVLMs on MMOral-Bench and find that even the best-performing model, i.e., GPT-4o, only achieves 41.45% accuracy, revealing significant limitations of current models in this domain. To promote the progress of this specific domain, we also propose OralGPT, which conducts supervised fine-tuning (SFT) upon Qwen2.5-VL-7B with our meticulously curated MMOral instruction dataset. Remarkably, a single epoch of SFT yields substantial performance enhancements for LVLMs, e.g., OralGPT demonstrates a 24.73% improvement. Both MMOral and OralGPT hold significant potential as a critical foundation for intelligent dentistry and enable more clinically impactful multimodal AI systems in the dental field. The dataset, model, benchmark, and evaluation suite are available at https://github.com/isbrycee/OralGPT.

