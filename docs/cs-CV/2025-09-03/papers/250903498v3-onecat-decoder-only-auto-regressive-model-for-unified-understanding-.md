---
layout: default
title: "OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation"
---

# OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03498" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03498v3</a>
  <a href="https://arxiv.org/pdf/2509.03498.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03498v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03498v3', 'OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Li, Xinyu Peng, Yaoming Wang, Zelin Peng, Xin Chen, Rongxiang Weng, Jingang Wang, Xunliang Cai, Wenrui Dai, Hongkai Xiong

**分类**: cs.CV

**发布日期**: 2025-09-03 (更新: 2025-10-07)

**备注**: technical report, project url:https://onecat-ai.github.io/

---

## 💡 一句话要点

**OneCAT：提出纯Decoder自回归多模态统一模型，实现高效理解、生成与编辑**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `自回归模型` `Decoder-Only` `混合专家` `统一建模` `视觉语言` `图像编辑`

## 📋 核心要点

1. 现有方法依赖ViT等外部视觉模块，推理效率低，尤其在高分辨率输入下。
2. OneCAT采用纯Decoder架构和模态特定MoE，以自回归方式统一建模理解、生成和编辑。
3. 实验表明，OneCAT在多模态生成、编辑和理解任务上超越现有开源模型，性能达到新高度。

## 📝 摘要（中文）

本文提出OneCAT，一个统一的多模态模型，它在一个新颖的、纯Decoder-Only Transformer架构中无缝集成了理解、生成和编辑能力。我们的框架独特地消除了推理期间对外部组件（如Vision Transformers (ViT) 或视觉tokenizer）的需求，从而显著提高了效率，尤其是在处理高分辨率输入时。这是通过一个特定模态的混合专家（MoE）结构实现的，该结构使用单一的自回归（AR）目标进行训练，并且原生支持动态分辨率。此外，我们在大型语言模型（LLM）中首创了一种多尺度视觉自回归机制，与基于扩散的方法相比，该机制大大减少了解码步骤，同时保持了最先进的性能。我们的研究结果表明，纯自回归建模作为统一多模态智能的充分而优雅的基础，具有强大的潜力。因此，OneCAT 设定了新的性能标准，在多模态生成、编辑和理解的基准测试中，优于现有的开源统一多模态模型。

## 🔬 方法详解

**问题定义**：现有统一多模态模型通常依赖于额外的视觉编码器（例如ViT）或视觉tokenizers，这增加了计算复杂性，尤其是在处理高分辨率图像时。这些额外的组件使得模型在推理阶段的效率降低，限制了其在实际应用中的部署。此外，如何有效地融合不同模态的信息，并实现理解、生成和编辑的统一建模仍然是一个挑战。

**核心思路**：OneCAT的核心思路是采用纯Decoder-Only的自回归模型，避免使用额外的视觉编码器或tokenizer。通过模态特定的混合专家（MoE）结构，模型可以学习不同模态的表示，并使用单一的自回归目标进行训练，从而实现理解、生成和编辑的统一建模。这种设计旨在提高推理效率，并简化模型结构。

**技术框架**：OneCAT的整体架构是一个纯Decoder-Only Transformer模型。它包含以下主要模块：1) 输入嵌入层：将不同模态（例如文本和图像）的输入转换为嵌入向量。2) 模态特定的混合专家（MoE）：每个模态都有自己的MoE模块，用于学习该模态的表示。3) Transformer Decoder层：使用标准的Transformer Decoder层进行自回归建模。4) 输出层：生成文本或图像的输出。模型使用单一的自回归目标进行训练，即预测下一个token或像素。

**关键创新**：OneCAT最重要的技术创新点在于其纯Decoder-Only的架构和模态特定的MoE结构。与现有方法相比，OneCAT不需要额外的视觉编码器或tokenizer，从而显著提高了推理效率。此外，OneCAT还引入了一种多尺度视觉自回归机制，可以减少解码步骤，同时保持高性能。

**关键设计**：OneCAT的关键设计包括：1) 模态特定的MoE结构：每个模态都有自己的MoE模块，可以更好地学习该模态的表示。2) 多尺度视觉自回归机制：通过在不同尺度上进行自回归建模，可以减少解码步骤。3) 损失函数：使用标准的自回归损失函数，即预测下一个token或像素的交叉熵损失。

## 📊 实验亮点

OneCAT在多项基准测试中取得了显著的成果。在多模态生成任务中，OneCAT优于现有的开源模型。在图像编辑任务中，OneCAT在保持图像质量的同时，能够实现更精确的编辑。在视觉问答任务中，OneCAT能够更准确地回答与图像相关的问题。这些结果表明，OneCAT在多模态理解、生成和编辑方面具有强大的能力。

## 🎯 应用场景

OneCAT具有广泛的应用前景，包括图像描述、视觉问答、图像编辑、多模态对话等。该模型的高效性和统一性使其能够应用于资源受限的设备上，例如移动设备和嵌入式系统。未来，OneCAT可以进一步扩展到其他模态，例如音频和视频，从而实现更全面的多模态智能。

## 📄 摘要（原文）

> We introduce OneCAT, a unified multimodal model that seamlessly integrates understanding, generation, and editing within a novel, pure decoder-only transformer architecture. Our framework uniquely eliminates the need for external components such as Vision Transformers (ViT) or vision tokenizer during inference, leading to significant efficiency gains, especially for high-resolution inputs. This is achieved through a modality-specific Mixture-of-Experts (MoE) structure trained with a single autoregressive (AR) objective, which also natively supports dynamic resolutions. Furthermore, we pioneer a multi-scale visual autoregressive mechanism within the Large Language Model (LLM) that drastically reduces decoding steps compared to diffusion-based methods while maintaining state-of-the-art performance. Our findings demonstrate the powerful potential of pure autoregressive modeling as a sufficient and elegant foundation for unified multimodal intelligence. As a result, OneCAT sets a new performance standard, outperforming existing open-source unified multimodal models across benchmarks for multimodal generation, editing, and understanding.

