---
layout: default
title: "FishAI 2.0: Marine Fish Image Classification with Multi-modal Few-shot Learning"
---

# FishAI 2.0: Marine Fish Image Classification with Multi-modal Few-shot Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22930" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22930v1</a>
  <a href="https://arxiv.org/pdf/2509.22930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22930v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22930v1', 'FishAI 2.0: Marine Fish Image Classification with Multi-modal Few-shot Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenghan Yang, Peng Zhou, Dong-Sheng Zhang, Yueyun Wang, Hong-Bin Shen, Xiaoyong Pan

**分类**: cs.CV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**FishAI 2.0：融合多模态少样本学习的海洋鱼类图像分类框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `海洋鱼类识别` `少样本学习` `多模态学习` `数据增强` `图像生成` `CLIP模型` `深度学习`

## 📋 核心要点

1. 传统海洋生物图像识别面临数据不完整和模型精度不足的挑战，尤其是在少样本情况下，数据稀缺严重影响性能。
2. FishAI 2.0通过结合大型语言模型生成文本描述，利用Stable Diffusion进行图像增强，构建多模态特征空间，提升少样本学习能力。
3. 实验结果表明，FishAI 2.0在科、属、种级别上均取得了显著的Top-1准确率，优于基线模型，具有实际应用价值。

## 📝 摘要（中文）

本研究针对海洋生物图像识别中数据集不完整和模型精度不理想的问题，尤其是在稀有物种的少样本条件下，数据稀缺严重阻碍了性能。为此，提出了一种智能海洋鱼类识别框架FishAI 2.0，该框架集成了多模态少样本深度学习技术和图像生成的数据增强方法。首先，利用分层海洋鱼类基准数据集训练FishAI 2.0模型，为后续模型训练提供全面的数据基础。为了解决稀有类别的数据稀缺问题，采用大型语言模型DeepSeek生成高质量的文本描述，并将其输入到Stable Diffusion 2中，通过分层扩散策略提取潜在编码，构建多模态特征空间，进行图像增强。然后，将增强的视觉-文本数据集输入到基于对比语言-图像预训练（CLIP）的模型中，实现鲁棒的少样本图像识别。实验结果表明，FishAI 2.0在科级水平上实现了91.67%的Top-1准确率和97.97%的Top-5准确率，显著优于基线CLIP和ViT模型，尤其是在训练样本少于10个的少数类别上。在属和种级别上，FishAI 2.0分别实现了87.58%和85.42%的Top-1准确率，展示了其在实际应用中的价值。总之，FishAI 2.0提高了海洋鱼类识别的效率和准确性，并为海洋生态监测和保护提供了可扩展的技术解决方案，突出了其科学价值和实际应用性。

## 🔬 方法详解

**问题定义**：论文旨在解决海洋鱼类图像识别中，由于数据稀缺，特别是稀有物种数据不足，导致传统图像识别模型在少样本学习场景下性能不佳的问题。现有方法难以有效利用有限的数据进行训练，泛化能力受限。

**核心思路**：论文的核心思路是利用多模态学习和数据增强技术，通过结合文本描述和图像生成，扩充训练数据集，并构建视觉-文本联合特征空间，从而提升模型在少样本条件下的识别能力。通过利用大型语言模型生成文本描述，再利用文本生成图像，从而缓解数据稀缺问题。

**技术框架**：FishAI 2.0框架主要包含以下几个阶段：1) 利用分层海洋鱼类基准数据集进行初始训练；2) 使用大型语言模型（DeepSeek）生成鱼类文本描述；3) 利用Stable Diffusion 2，将文本描述转化为图像，进行数据增强；4) 将增强后的视觉-文本数据集输入到基于CLIP的模型中进行训练；5) 利用训练好的模型进行少样本图像识别。

**关键创新**：该论文的关键创新在于结合了大型语言模型和扩散模型进行数据增强，构建了多模态特征空间，从而有效提升了少样本学习的性能。与传统的数据增强方法相比，该方法能够生成更具多样性和信息量的图像，从而更好地提升模型的泛化能力。

**关键设计**：论文采用了分层扩散策略，提取潜在编码来构建多模态特征空间。具体来说，DeepSeek用于生成高质量的文本描述，这些描述被输入到Stable Diffusion 2中，通过控制扩散过程的参数，生成与原始图像风格一致的新图像。此外，基于CLIP的模型被用于学习视觉和文本之间的对应关系，从而实现鲁棒的少样本图像识别。

## 📊 实验亮点

FishAI 2.0在科级水平上实现了91.67%的Top-1准确率和97.97%的Top-5准确率，显著优于基线CLIP和ViT模型。尤其是在训练样本少于10个的少数类别上，性能提升更为明显。在属和种级别上，FishAI 2.0分别实现了87.58%和85.42%的Top-1准确率，展示了其在实际应用中的潜力。

## 🎯 应用场景

FishAI 2.0可应用于海洋生态监测、渔业资源管理、水产养殖等领域。通过提高海洋鱼类识别的效率和准确性，有助于更好地了解海洋生态系统的健康状况，为海洋保护和可持续利用提供技术支持。该研究具有重要的科学价值和实际应用前景，有望推动海洋生物多样性保护和管理。

## 📄 摘要（原文）

> Traditional marine biological image recognition faces challenges of incomplete datasets and unsatisfactory model accuracy, particularly for few-shot conditions of rare species where data scarcity significantly hampers the performance. To address these issues, this study proposes an intelligent marine fish recognition framework, FishAI 2.0, integrating multimodal few-shot deep learning techniques with image generation for data augmentation. First, a hierarchical marine fish benchmark dataset, which provides a comprehensive data foundation for subsequent model training, is utilized to train the FishAI 2.0 model. To address the data scarcity of rare classes, the large language model DeepSeek was employed to generate high-quality textual descriptions, which are input into Stable Diffusion 2 for image augmentation through a hierarchical diffusion strategy that extracts latent encoding to construct a multimodal feature space. The enhanced visual-textual datasets were then fed into a Contrastive Language-Image Pre-Training (CLIP) based model, enabling robust few-shot image recognition. Experimental results demonstrate that FishAI 2.0 achieves a Top-1 accuracy of 91.67 percent and Top-5 accuracy of 97.97 percent at the family level, outperforming baseline CLIP and ViT models with a substantial margin for the minority classes with fewer than 10 training samples. To better apply FishAI 2.0 to real-world scenarios, at the genus and species level, FishAI 2.0 respectively achieves a Top-1 accuracy of 87.58 percent and 85.42 percent, demonstrating practical utility. In summary, FishAI 2.0 improves the efficiency and accuracy of marine fish identification and provides a scalable technical solution for marine ecological monitoring and conservation, highlighting its scientific value and practical applicability.

