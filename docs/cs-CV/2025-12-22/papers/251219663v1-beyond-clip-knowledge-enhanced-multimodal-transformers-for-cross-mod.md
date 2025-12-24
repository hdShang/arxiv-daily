---
layout: default
title: "Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis"
---

# Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19663" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19663v1</a>
  <a href="https://arxiv.org/pdf/2512.19663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19663v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19663v1', 'Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Argha Kamal Samanta, Harshika Goyal, Vasudha Joshi, Tushar Mungle, Pabitra Mitra

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-22

**备注**: 14 pages, 14 figures

---

## 💡 一句话要点

**提出知识增强多模态Transformer，用于糖尿病视网膜病变诊断中的跨模态对齐**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `糖尿病视网膜病变` `多模态学习` `跨模态对齐` `医学图像分析` `知识增强` `Transformer` `对比学习`

## 📋 核心要点

1. 现有CLIP等视觉-语言模型在医学图像跨模态检索方面表现不佳，无法有效对齐图像和临床文本。
2. 提出一种知识增强的多模态Transformer框架，融合视网膜图像、临床文本和结构化数据，实现跨模态对齐。
3. 在BRSET数据集上，文本到图像检索Recall@1达到99.94%，显著优于微调的CLIP，并在DeepEyeNet数据集上展现出强大的泛化能力。

## 📝 摘要（中文）

糖尿病视网膜病变(DR)是全球可预防性失明的主要原因，需要精确的自动化诊断系统。通用领域的视觉-语言模型（如CLIP）在自然图像任务中表现良好，但在医学领域应用中表现不佳，尤其是在眼科图像的跨模态检索方面。我们提出了一种新颖的知识增强联合嵌入框架，该框架通过多模态Transformer架构整合视网膜眼底图像、临床文本和结构化患者数据，以解决医学图像-文本对齐的关键差距。我们的方法为每个模态采用单独的编码器：用于视网膜图像的Vision Transformer (ViT-B/16)、用于临床叙述的Bio-ClinicalBERT以及用于结构化人口统计学和临床特征的多层感知器。这些模态通过具有模态特定嵌入的联合Transformer融合，并使用包括模态对之间的对比损失、图像和文本的重建损失以及根据ICDR和SDRG方案进行DR严重程度分级的分类损失在内的多个目标进行训练。在巴西多标签眼科数据集(BRSET)上的实验结果表明，与基线模型相比，有显著的改进。我们的框架实现了近乎完美的文本到图像检索性能，Recall@1为99.94%，而微调的CLIP为1.29%，同时保持了最先进的SDRG分类精度97.05%和ICDR分类精度97.97%。此外，在未见过的DeepEyeNet数据集上的零样本评估验证了强大的泛化能力，Recall@1为93.95%，而微调的CLIP为0.22%。这些结果表明，我们的多模态训练方法有效地捕捉了医学领域的跨模态关系，从而建立了卓越的检索能力和强大的诊断性能。

## 🔬 方法详解

**问题定义**：论文旨在解决糖尿病视网膜病变（DR）诊断中，医学图像（眼底图像）与临床文本信息之间跨模态对齐的问题。现有方法，如直接使用通用视觉-语言模型（如CLIP）进行微调，在医学领域表现不佳，无法有效捕捉图像和文本之间的复杂关系，导致检索和诊断性能下降。

**核心思路**：论文的核心思路是利用知识增强的多模态Transformer架构，显式地融合来自不同模态（图像、文本、结构化数据）的信息，并通过多目标学习策略，促使模型学习到更鲁棒和准确的跨模态表示。通过引入医学领域的先验知识，提升模型在特定任务上的性能。

**技术框架**：整体框架包含三个主要模块：1) 模态编码器：分别使用ViT-B/16编码眼底图像，Bio-ClinicalBERT编码临床文本，多层感知器（MLP）编码结构化数据。2) 联合Transformer：将不同模态的嵌入向量输入到联合Transformer中，进行跨模态特征融合。3) 多目标学习：使用对比损失（模态对之间）、重建损失（图像和文本）和分类损失（DR严重程度分级）进行联合训练。

**关键创新**：最重要的技术创新点在于知识增强的多模态融合方法。与直接微调通用模型不同，该方法针对医学领域特点，设计了专门的模态编码器（如Bio-ClinicalBERT）和多目标学习策略，从而更好地捕捉医学图像和文本之间的关联。

**关键设计**：关键设计包括：1) 使用Bio-ClinicalBERT作为文本编码器，利用生物医学领域的预训练知识。2) 设计了多目标损失函数，包括对比损失、重建损失和分类损失，以促进跨模态对齐和诊断性能。3) 使用模态特定的嵌入，更好地表示不同模态的信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19663v1/dr_grades_distribution_log.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19663v1/anatomical_status_distribution.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19663v1/other_pathological_features_prevalence.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在BRSET数据集上实现了近乎完美的文本到图像检索性能，Recall@1达到99.94%，显著优于微调的CLIP（1.29%）。同时，在SDRG和ICDR分类任务中，分别取得了97.05%和97.97%的分类精度。在未见过的DeepEyeNet数据集上的零样本评估中，Recall@1为93.95%，远超微调的CLIP（0.22%），验证了模型的泛化能力。

## 🎯 应用场景

该研究成果可应用于糖尿病视网膜病变的自动化诊断系统，辅助医生进行快速准确的诊断，尤其是在医疗资源匮乏的地区。此外，该方法也可推广到其他医学图像-文本对齐任务，例如放射学报告生成、病理图像分析等，具有广泛的应用前景。

## 📄 摘要（原文）

> Diabetic retinopathy (DR) is a leading cause of preventable blindness worldwide, demanding accurate automated diagnostic systems. While general-domain vision-language models like Contrastive Language-Image Pre-Training (CLIP) perform well on natural image tasks, they struggle in medical domain applications, particularly in cross-modal retrieval for ophthalmological images. We propose a novel knowledge-enhanced joint embedding framework that integrates retinal fundus images, clinical text, and structured patient data through a multimodal transformer architecture to address the critical gap in medical image-text alignment. Our approach employs separate encoders for each modality: a Vision Transformer (ViT-B/16) for retinal images, Bio-ClinicalBERT for clinical narratives, and a multilayer perceptron for structured demographic and clinical features. These modalities are fused through a joint transformer with modality-specific embeddings, trained using multiple objectives including contrastive losses between modality pairs, reconstruction losses for images and text, and classification losses for DR severity grading according to ICDR and SDRG schemes. Experimental results on the Brazilian Multilabel Ophthalmological Dataset (BRSET) demonstrate significant improvements over baseline models. Our framework achieves near-perfect text-to-image retrieval performance with Recall@1 of 99.94% compared to fine-tuned CLIP's 1.29%, while maintaining state-of-the-art classification accuracy of 97.05% for SDRG and 97.97% for ICDR. Furthermore, zero-shot evaluation on the unseen DeepEyeNet dataset validates strong generalizability with 93.95% Recall@1 versus 0.22% for fine-tuned CLIP. These results demonstrate that our multimodal training approach effectively captures cross-modal relationships in the medical domain, establishing both superior retrieval capabilities and robust diagnostic performance.

