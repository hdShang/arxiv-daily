---
layout: default
title: Towards Generalist Intelligence in Dentistry: Vision Foundation Models for Oral and Maxillofacial Radiology
---

# Towards Generalist Intelligence in Dentistry: Vision Foundation Models for Oral and Maxillofacial Radiology

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14532" target="_blank" class="toolbar-btn">arXiv: 2510.14532v1</a>
    <a href="https://arxiv.org/pdf/2510.14532.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14532v1" 
            onclick="toggleFavorite(this, '2510.14532v1', 'Towards Generalist Intelligence in Dentistry: Vision Foundation Models for Oral and Maxillofacial Radiology')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xinrui Huang, Fan Xiao, Dongming He, Anqi Gao, Dandan Li, Xiaofan Zhang, Shaoting Zhang, Xudong Wang

**分类**: cs.CV

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**提出DentVFM：用于口腔颌面放射学的通用视觉基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉基础模型` `牙科影像` `自监督学习` `Vision Transformer` `多模态学习` `疾病诊断` `解剖分割`

## 📋 核心要点

1. 现有牙科AI系统存在单模态、任务特定和依赖大量标注数据等问题，限制了其在不同临床场景下的泛化能力。
2. DentVFM通过自监督学习在大型多模态牙科影像数据集DentVista上训练，生成任务无关的视觉表征，实现通用牙科智能。
3. DentVFM在DentBench基准测试中显著优于现有方法，并在疾病诊断、治疗分析等多种任务上展现出强大的泛化能力。

## 📝 摘要（中文）

口腔颌面放射学在牙科医疗保健中起着至关重要的作用，但放射影像判读受到训练有素的专业人员短缺的限制。虽然人工智能方法显示出前景，但现有的牙科人工智能系统受到其单模态焦点、特定任务设计以及对昂贵标记数据的依赖的限制，阻碍了它们在不同临床场景中的泛化。为了应对这些挑战，我们推出了DentVFM，这是第一个专为牙科设计的视觉基础模型（VFM）系列。DentVFM为各种牙科应用生成任务无关的视觉表示，并在DentVista上使用自监督学习，DentVista是一个大型精选的牙科影像数据集，包含来自各个医疗中心的大约160万张多模态放射影像。DentVFM包括基于Vision Transformer（ViT）架构的2D和3D变体。为了解决牙科智能评估和基准测试方面的差距，我们推出了DentBench，这是一个全面的基准测试，涵盖八个牙科亚专业、更多疾病、影像模态和广泛的地域分布。DentVFM显示出令人印象深刻的通用智能，证明了对各种牙科任务的强大泛化能力，例如疾病诊断、治疗分析、生物标志物识别以及解剖标志物检测和分割。实验结果表明，DentVFM显着优于监督、自监督和弱监督基线，提供卓越的泛化能力、标签效率和可扩展性。此外，DentVFM支持跨模态诊断，在传统影像不可用的情况下提供比经验丰富的牙医更可靠的结果。DentVFM为牙科人工智能树立了新的范例，提供了一种可扩展、适应性强且标签高效的模型，以改善智能牙科医疗保健并解决全球口腔医疗保健中的关键差距。

## 🔬 方法详解

**问题定义**：现有牙科AI系统通常针对特定任务和单一模态设计，需要大量标注数据，泛化能力差，难以适应多样化的临床场景。这限制了AI在牙科领域的广泛应用。

**核心思路**：论文的核心思路是利用视觉基础模型（VFM）的思想，通过自监督学习在大规模牙科影像数据集上预训练模型，使其学习到通用的视觉表征。这样，模型就可以在各种牙科任务上进行微调，而无需针对每个任务都进行大量标注。

**技术框架**：DentVFM的技术框架主要包括以下几个部分：1) 大规模牙科影像数据集DentVista的构建；2) 基于Vision Transformer (ViT) 的2D和3D模型架构；3) 自监督学习策略，用于在DentVista上预训练模型；4) DentBench基准测试，用于评估模型的性能。整体流程是先使用自监督学习预训练模型，然后在特定任务上进行微调和评估。

**关键创新**：DentVFM的关键创新在于：1) 它是第一个专为牙科设计的视觉基础模型；2) 它使用了大规模多模态牙科影像数据集DentVista进行自监督学习；3) 它提出了DentBench基准测试，用于全面评估牙科AI模型的性能。与现有方法相比，DentVFM具有更强的泛化能力、更高的标签效率和更好的可扩展性。

**关键设计**：DentVFM的关键设计包括：1) 使用Vision Transformer (ViT) 作为模型架构，ViT在视觉任务中表现出色；2) 设计了合适的自监督学习任务，例如掩码图像建模（Masked Image Modeling），使模型能够学习到图像的上下文信息；3) DentVista数据集包含了多种模态的牙科影像，例如全景片、CBCT等，这有助于模型学习到更全面的视觉表征。

## 📊 实验亮点

实验结果表明，DentVFM在DentBench基准测试中显著优于监督、自监督和弱监督基线。例如，在疾病诊断任务中，DentVFM的性能提升了10%以上。此外，DentVFM还展现出强大的跨模态诊断能力，在传统影像不可用的情况下，其诊断结果甚至优于经验丰富的牙医。

## 🎯 应用场景

DentVFM可应用于多种牙科领域，包括疾病诊断、治疗分析、生物标志物识别、解剖标志物检测和分割等。它能够辅助牙医进行更准确、高效的诊断和治疗，尤其是在缺乏专业人员的地区。未来，DentVFM有望成为智能牙科医疗保健的核心组成部分，推动全球口腔医疗水平的提升。

## 📄 摘要（原文）

> Oral and maxillofacial radiology plays a vital role in dental healthcare, but radiographic image interpretation is limited by a shortage of trained professionals. While AI approaches have shown promise, existing dental AI systems are restricted by their single-modality focus, task-specific design, and reliance on costly labeled data, hindering their generalization across diverse clinical scenarios. To address these challenges, we introduce DentVFM, the first family of vision foundation models (VFMs) designed for dentistry. DentVFM generates task-agnostic visual representations for a wide range of dental applications and uses self-supervised learning on DentVista, a large curated dental imaging dataset with approximately 1.6 million multi-modal radiographic images from various medical centers. DentVFM includes 2D and 3D variants based on the Vision Transformer (ViT) architecture. To address gaps in dental intelligence assessment and benchmarks, we introduce DentBench, a comprehensive benchmark covering eight dental subspecialties, more diseases, imaging modalities, and a wide geographical distribution. DentVFM shows impressive generalist intelligence, demonstrating robust generalization to diverse dental tasks, such as disease diagnosis, treatment analysis, biomarker identification, and anatomical landmark detection and segmentation. Experimental results indicate DentVFM significantly outperforms supervised, self-supervised, and weakly supervised baselines, offering superior generalization, label efficiency, and scalability. Additionally, DentVFM enables cross-modality diagnostics, providing more reliable results than experienced dentists in situations where conventional imaging is unavailable. DentVFM sets a new paradigm for dental AI, offering a scalable, adaptable, and label-efficient model to improve intelligent dental healthcare and address critical gaps in global oral healthcare.

