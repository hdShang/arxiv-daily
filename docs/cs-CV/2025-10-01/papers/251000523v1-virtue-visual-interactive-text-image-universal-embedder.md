---
layout: default
title: VIRTUE: Visual-Interactive Text-Image Universal Embedder
---

# VIRTUE: Visual-Interactive Text-Image Universal Embedder

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00523" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00523v1</a>
  <a href="https://arxiv.org/pdf/2510.00523.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00523v1" onclick="toggleFavorite(this, '2510.00523v1', 'VIRTUE: Visual-Interactive Text-Image Universal Embedder')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei-Yao Wang, Kazuya Tateishi, Qiyu Wu, Shusuke Takahashi, Yuki Mitsufuji

**分类**: cs.AI, cs.CV

**发布日期**: 2025-10-01

**备注**: 25 pages

---

## 💡 一句话要点

**提出VIRTUE：一种视觉交互式文本-图像通用嵌入模型，提升多模态表征能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉交互` `文本图像嵌入` `多模态学习` `分割模型` `视觉语言模型` `表征学习` `人机交互`

## 📋 核心要点

1. 现有嵌入模型缺乏视觉交互能力，无法根据用户指定的图像区域进行精确嵌入，限制了其在人机交互场景中的应用。
2. VIRTUE通过集成分割模型和视觉-语言模型，使嵌入器能够处理视觉提示，从而精确定位图像中的特定区域，提升表征学习能力。
3. 在包含100万样本的SCaR基准测试中，VIRTUE在多个任务上取得了显著的性能提升，证明了其视觉交互能力的有效性。

## 📝 摘要（中文）

多模态表征学习模型在复杂任务中表现出色，视觉-语言模型（VLM）的集成进一步使嵌入模型具备了指令跟随能力。然而，现有的嵌入模型缺乏视觉交互能力，无法指定用户感兴趣的区域（例如，点、边界框、掩码），而这种能力已经在生成模型中得到探索，以扩展其人机交互适用性。为嵌入模型配备视觉交互能力不仅可以解锁新的应用，实现用户意图的局部化定位，这仍然是一个未被探索的领域，还可以使模型学习图像中的实体级别信息，以补充其用于传统嵌入任务的全局表征。在本文中，我们提出了一种新的视觉交互式文本-图像通用嵌入器（VIRTUE），它将分割模型和视觉-语言模型的能力扩展到表征学习领域。在VIRTUE中，分割模型可以处理视觉提示，精确定位图像中的特定区域，从而使嵌入器能够更精确地处理复杂和模糊的场景。为了评估VIRTUE的视觉交互能力，我们引入了一个大规模的分割和场景字幕检索（SCaR）基准，包含100万个样本，旨在通过联合考虑具有特定对象和图像场景的实体来检索文本字幕。VIRTUE在36个通用MMEB任务（3.1%-8.5%）和5个视觉交互式SCaR任务（15.2%-20.3%）中始终如一地实现了最先进的性能，并取得了显著的改进。

## 🔬 方法详解

**问题定义**：现有文本-图像嵌入模型主要关注全局图像特征，缺乏对用户指定图像区域的交互能力。这限制了模型在需要精细化理解和定位用户意图的场景下的应用，例如，根据用户点击的物体检索相关文本描述。现有方法无法有效利用视觉提示信息，导致在复杂场景下表现不佳。

**核心思路**：VIRTUE的核心思路是将分割模型与视觉-语言模型相结合，利用分割模型处理视觉提示，从而精确定位图像中的特定区域。通过这种方式，模型可以学习到更细粒度的实体级别信息，并将其融入到全局表征中，从而提升嵌入的准确性和交互性。

**技术框架**：VIRTUE包含三个主要模块：视觉提示处理模块、图像编码模块和文本编码模块。视觉提示处理模块利用分割模型处理用户提供的视觉提示（如点、边界框、掩码），提取感兴趣区域的特征。图像编码模块负责提取全局图像特征。文本编码模块负责提取文本描述的特征。最终，模型将视觉提示特征、全局图像特征和文本特征融合，生成最终的嵌入向量。

**关键创新**：VIRTUE的关键创新在于将分割模型引入到文本-图像嵌入框架中，使其具备了视觉交互能力。这使得模型能够根据用户指定的图像区域进行精确嵌入，从而更好地理解用户意图。此外，VIRTUE还引入了一个大规模的分割和场景字幕检索（SCaR）基准，用于评估模型的视觉交互能力。

**关键设计**：VIRTUE使用了预训练的视觉-语言模型作为基础架构，并在此基础上进行了微调。分割模型采用了Mask2Former。损失函数包括对比损失和交叉熵损失，用于优化嵌入向量的相似性和分类性能。视觉提示的编码方式采用了RoI Align。

## 📊 实验亮点

VIRTUE在36个通用MMEB任务上取得了3.1%-8.5%的性能提升，在5个视觉交互式SCaR任务上取得了15.2%-20.3%的显著提升。这些结果表明，VIRTUE的视觉交互能力能够有效提升多模态表征学习的性能，尤其是在需要精细化理解和定位用户意图的场景下。

## 🎯 应用场景

VIRTUE可应用于图像检索、视觉问答、人机交互等领域。例如，在电商场景中，用户可以通过点击商品图片中的特定区域来搜索相似商品；在智能客服场景中，可以通过视觉提示引导模型理解用户意图，从而提供更准确的答案。该研究有望推动多模态交互式人工智能的发展。

## 📄 摘要（原文）

> Multimodal representation learning models have demonstrated successful operation across complex tasks, and the integration of vision-language models (VLMs) has further enabled embedding models with instruction-following capabilities. However, existing embedding models lack visual-interactive capabilities to specify regions of interest from users (e.g., point, bounding box, mask), which have been explored in generative models to broaden their human-interactive applicability. Equipping embedding models with visual interactions not only would unlock new applications with localized grounding of user intent, which remains unexplored, but also enable the models to learn entity-level information within images to complement their global representations for conventional embedding tasks. In this paper, we propose a novel Visual-InteRactive Text-Image Universal Embedder (VIRTUE) that extends the capabilities of the segmentation model and the vision-language model to the realm of representation learning. In VIRTUE, the segmentation model can process visual prompts that pinpoint specific regions within an image, thereby enabling the embedder to handle complex and ambiguous scenarios more precisely. To evaluate the visual-interaction ability of VIRTUE, we introduce a large-scale Segmentation-and-Scene Caption Retrieval (SCaR) benchmark comprising 1M samples that aims to retrieve the text caption by jointly considering the entity with a specific object and image scene. VIRTUE consistently achieves a state-of-the-art performance with significant improvements across 36 universal MMEB (3.1%-8.5%) and five visual-interactive SCaR (15.2%-20.3%) tasks.

