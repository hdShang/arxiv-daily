---
layout: default
title: "GAMMA: Generalizable Alignment via Multi-task and Manipulation-Augmented Training for AI-Generated Image Detection"
---

# GAMMA: Generalizable Alignment via Multi-task and Manipulation-Augmented Training for AI-Generated Image Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10250" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10250v1</a>
  <a href="https://arxiv.org/pdf/2509.10250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10250v1', 'GAMMA: Generalizable Alignment via Multi-task and Manipulation-Augmented Training for AI-Generated Image Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhen Yan, Yan Hong, Suning Lang, Jiahui Zhan, Yikun Ji, Yujie Gao, Jun Lan, Huijia Zhu, Weiqiang Wang, Jianfu Zhang

**分类**: cs.CV

**发布日期**: 2025-09-12

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**GAMMA：通过多任务和操纵增强训练实现AI生成图像检测的泛化对齐**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `AI生成图像检测` `泛化能力` `多任务学习` `操纵增强` `反向交叉注意力`

## 📋 核心要点

1. 现有AI生成图像检测器依赖于生成模型的特定伪影，泛化能力不足，难以应对新型生成模型。
2. GAMMA框架通过多任务学习和操纵增强训练，减少领域偏差，增强语义对齐，提升模型泛化能力。
3. 实验表明，GAMMA在GenImage基准测试中取得了SOTA的泛化性能，并在GPT-4o等新模型上保持了鲁棒性。

## 📝 摘要（中文）

随着生成模型变得越来越复杂和多样化，检测AI生成的图像变得越来越具有挑战性。现有的AI生成图像检测器在同分布生成图像上取得了有希望的性能，但它们对未见过的生成模型的泛化能力仍然有限。这种局限性主要归因于它们对特定于生成的伪影的依赖，例如风格先验和压缩模式。为了解决这些限制，我们提出了一种新的训练框架GAMMA，旨在减少领域偏差并增强语义对齐。GAMMA引入了多种操纵策略，例如基于修复的操纵和语义保持扰动，以确保操纵内容和真实内容之间的一致性。我们采用具有双分割头和分类头的多任务监督，从而能够在不同的生成域中进行像素级源属性归因。此外，引入了一种反向交叉注意力机制，以允许分割头指导和纠正分类分支中的有偏表示。我们的方法在GenImage基准测试中实现了最先进的泛化性能，提高了5.8%的准确率，并且在新发布的生成模型（如GPT-4o）上保持了强大的鲁棒性。

## 🔬 方法详解

**问题定义**：现有AI生成图像检测方法过度依赖特定生成模型的风格先验和压缩模式等伪影，导致模型在面对未知的生成模型时泛化能力显著下降。这些方法难以有效区分真实图像和新型AI生成图像，限制了其在实际应用中的可靠性。

**核心思路**：GAMMA的核心思路是通过操纵增强训练和多任务学习，使模型学习到更通用的、与生成模型无关的图像特征。通过引入多种操纵策略，迫使模型关注图像的语义一致性，而非特定生成器的伪影。多任务学习则通过像素级的源属性归因，增强模型对图像来源的理解。

**技术框架**：GAMMA的整体框架包括三个主要组成部分：操纵增强模块、多任务学习模块和反向交叉注意力模块。操纵增强模块负责生成各种被操纵的图像，包括基于修复的操纵和语义保持扰动。多任务学习模块包含一个分类头和两个分割头，分别用于图像分类和像素级源属性分割。反向交叉注意力模块则用于将分割头的知识传递给分类头，以纠正分类分支中的有偏表示。

**关键创新**：GAMMA的关键创新在于其操纵增强训练策略和反向交叉注意力机制。操纵增强训练通过引入多种操纵方式，迫使模型学习更鲁棒的特征表示，减少对特定生成器伪影的依赖。反向交叉注意力机制则允许分割头指导分类头，从而提高分类的准确性。

**关键设计**：GAMMA的关键设计包括：1) 多样化的操纵策略，例如in-painting和语义保持扰动，以模拟真实世界中的图像篡改；2) 双分割头的设计，用于提供像素级别的源属性信息；3) 反向交叉注意力机制，通过分割头来指导分类头，从而纠正分类偏差；4) 多任务损失函数，结合了分类损失和分割损失，以优化模型的整体性能。

## 📊 实验亮点

GAMMA在GenImage基准测试中取得了显著的性能提升，准确率提高了5.8%，达到了SOTA水平。此外，该方法在应对新发布的生成模型（如GPT-4o）时，仍然表现出强大的鲁棒性，表明其具有良好的泛化能力。这些实验结果验证了GAMMA框架在减少领域偏差和增强语义对齐方面的有效性。

## 🎯 应用场景

GAMMA的研究成果可应用于内容安全领域，例如检测社交媒体上的AI生成虚假信息、保护知识产权、防止恶意软件传播等。该技术还有助于提高数字取证的效率和准确性，为维护网络安全和社会稳定提供技术支持。未来，该技术可以进一步扩展到视频、音频等其他模态的AI生成内容检测。

## 📄 摘要（原文）

> With generative models becoming increasingly sophisticated and diverse, detecting AI-generated images has become increasingly challenging. While existing AI-genereted Image detectors achieve promising performance on in-distribution generated images, their generalization to unseen generative models remains limited. This limitation is largely attributed to their reliance on generation-specific artifacts, such as stylistic priors and compression patterns. To address these limitations, we propose GAMMA, a novel training framework designed to reduce domain bias and enhance semantic alignment. GAMMA introduces diverse manipulation strategies, such as inpainting-based manipulation and semantics-preserving perturbations, to ensure consistency between manipulated and authentic content. We employ multi-task supervision with dual segmentation heads and a classification head, enabling pixel-level source attribution across diverse generative domains. In addition, a reverse cross-attention mechanism is introduced to allow the segmentation heads to guide and correct biased representations in the classification branch. Our method achieves state-of-the-art generalization performance on the GenImage benchmark, imporving accuracy by 5.8%, but also maintains strong robustness on newly released generative model such as GPT-4o.

