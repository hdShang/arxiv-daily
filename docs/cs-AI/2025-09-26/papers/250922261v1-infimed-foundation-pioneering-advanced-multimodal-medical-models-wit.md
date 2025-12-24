---
layout: default
title: "InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning"
---

# InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22261" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22261v1</a>
  <a href="https://arxiv.org/pdf/2509.22261.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22261v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22261v1', 'InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanghao Zhu, Zhitian Hou, Zeyu Liu, Zhijie Sang, Congkai Xie, Hongxia Yang

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-26

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/InfiX-ai/InfiMed-Foundation-4B)

---

## 💡 一句话要点

**InfiMed-Foundation：通过高效预训练和多阶段微调，构建先进的多模态医学模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态医学模型` `大型语言模型` `预训练` `微调` `医学视觉问答` `医学诊断` `数据质量评估`

## 📋 核心要点

1. 通用多模态大语言模型缺乏医学领域专业知识，知识蒸馏难以捕捉医学领域特定知识，大规模医学数据持续预训练计算成本高昂。
2. 提出InfiMed-Foundation系列模型，结合高质量通用和医学多模态数据，采用五维质量评估框架，并使用低到高分辨率图像和多模态序列打包提高训练效率。
3. InfiMed-Foundation-1.7B优于Qwen2.5VL-3B，InfiMed-Foundation-4B超过HuatuoGPT-V-7B和MedGemma-27B-IT，在医学视觉问答和诊断任务中表现出色。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在各个领域都显示出巨大的潜力，但它们在医学领域的应用受到一些挑战的阻碍。通用MLLM通常缺乏医学任务所需的专业知识，导致不确定或虚假的回答。从先进模型中进行知识蒸馏难以捕捉放射学和药理学中的领域特定知识。此外，使用大规模医学数据进行持续预训练的计算成本带来了巨大的效率挑战。为了解决这些问题，我们提出了InfiMed-Foundation-1.7B和InfiMed-Foundation-4B，这两种医学专用MLLM旨在提供医学应用中最先进的性能。我们结合了高质量的通用和医学多模态数据，并提出了一个新颖的五维质量评估框架来管理高质量的多模态医学数据集。我们采用由低到高的图像分辨率和多模态序列打包来提高训练效率，从而能够整合广泛的医学数据。此外，一个三阶段的监督微调过程确保了复杂医学任务的有效知识提取。在MedEvalKit框架上评估，InfiMed-Foundation-1.7B优于Qwen2.5VL-3B，而InfiMed-Foundation-4B超过了HuatuoGPT-V-7B和MedGemma-27B-IT，证明了其在医学视觉问答和诊断任务中的卓越性能。通过解决数据质量、训练效率和领域特定知识提取方面的关键挑战，我们的工作为医疗保健领域更可靠、更有效的AI驱动解决方案铺平了道路。

## 🔬 方法详解

**问题定义**：现有通用多模态大语言模型在医学领域应用受限，主要痛点在于缺乏医学专业知识，容易产生不确定或错误的回答。知识蒸馏方法难以有效迁移医学领域的专业知识，而直接在大规模医学数据上进行预训练又面临计算资源和效率的挑战。

**核心思路**：InfiMed-Foundation的核心思路是构建医学领域专用的多模态大语言模型，通过高质量的数据筛选、高效的训练策略和多阶段的微调方法，使模型能够更好地理解和处理医学图像和文本信息，从而在医学视觉问答和诊断等任务中取得更好的性能。

**技术框架**：InfiMed-Foundation的整体框架包括数据准备、预训练和微调三个主要阶段。数据准备阶段，收集通用和医学多模态数据，并采用五维质量评估框架进行筛选。预训练阶段，采用低到高图像分辨率和多模态序列打包技术提高训练效率。微调阶段，采用三阶段监督微调策略，逐步提升模型在特定医学任务上的性能。

**关键创新**：该论文的关键创新点在于：1) 提出了一个五维质量评估框架，用于筛选高质量的医学多模态数据；2) 采用了低到高图像分辨率和多模态序列打包技术，显著提高了训练效率；3) 设计了一个三阶段的监督微调策略，有效提升了模型在医学任务上的性能。与现有方法相比，InfiMed-Foundation更注重数据质量和训练效率，并针对医学领域的特点进行了优化。

**关键设计**：五维质量评估框架包括数据完整性、准确性、一致性、相关性和可读性五个维度。低到高图像分辨率训练策略从低分辨率图像开始，逐步增加分辨率，以减少计算量和提高训练稳定性。多模态序列打包技术将多个图像和文本序列打包成一个序列进行训练，以提高训练效率。三阶段微调策略包括：第一阶段，使用大规模医学数据进行预训练；第二阶段，使用特定任务的数据进行微调；第三阶段，使用少量高质量数据进行精调。

## 📊 实验亮点

InfiMed-Foundation在MedEvalKit框架上进行了评估，结果表明，InfiMed-Foundation-1.7B的性能优于Qwen2.5VL-3B，而InfiMed-Foundation-4B的性能超过了HuatuoGPT-V-7B和MedGemma-27B-IT。这些结果表明，InfiMed-Foundation在医学视觉问答和诊断任务中具有显著的优势。

## 🎯 应用场景

InfiMed-Foundation在医疗领域具有广泛的应用前景，例如辅助医学诊断、医学影像报告生成、医学知识问答、患者咨询等。该研究可以帮助医生更准确、更高效地进行诊断和治疗，提高医疗服务质量，并为患者提供更便捷的医疗咨询服务。未来，该模型有望应用于远程医疗、智能健康管理等领域，推动医疗行业的智能化发展。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have shown remarkable potential in various domains, yet their application in the medical field is hindered by several challenges. General-purpose MLLMs often lack the specialized knowledge required for medical tasks, leading to uncertain or hallucinatory responses. Knowledge distillation from advanced models struggles to capture domain-specific expertise in radiology and pharmacology. Additionally, the computational cost of continual pretraining with large-scale medical data poses significant efficiency challenges. To address these issues, we propose InfiMed-Foundation-1.7B and InfiMed-Foundation-4B, two medical-specific MLLMs designed to deliver state-of-the-art performance in medical applications. We combined high-quality general-purpose and medical multimodal data and proposed a novel five-dimensional quality assessment framework to curate high-quality multimodal medical datasets. We employ low-to-high image resolution and multimodal sequence packing to enhance training efficiency, enabling the integration of extensive medical data. Furthermore, a three-stage supervised fine-tuning process ensures effective knowledge extraction for complex medical tasks. Evaluated on the MedEvalKit framework, InfiMed-Foundation-1.7B outperforms Qwen2.5VL-3B, while InfiMed-Foundation-4B surpasses HuatuoGPT-V-7B and MedGemma-27B-IT, demonstrating superior performance in medical visual question answering and diagnostic tasks. By addressing key challenges in data quality, training efficiency, and domain-specific knowledge extraction, our work paves the way for more reliable and effective AI-driven solutions in healthcare. InfiMed-Foundation-4B model is available at \href{https://huggingface.co/InfiX-ai/InfiMed-Foundation-4B}{InfiMed-Foundation-4B}.

