---
layout: default
title: "SMooGPT: Stylized Motion Generation using Large Language Models"
---

# SMooGPT: Stylized Motion Generation using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04058" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04058v1</a>
  <a href="https://arxiv.org/pdf/2509.04058.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04058v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04058v1', 'SMooGPT: Stylized Motion Generation using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Zhong, Yi Yang, Changjian Li

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出SMooGPT，利用大型语言模型实现可控、可解释的风格化动作生成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `风格化动作生成` `大型语言模型` `动作合成` `文本驱动生成` `身体部位建模`

## 📋 核心要点

1. 现有风格化动作生成方法可解释性差，泛化性有限，且受限于数据集偏差，难以生成多样动作。
2. SMooGPT 利用大型语言模型，将动作分解为身体部位文本描述，实现推理、组合和生成。
3. 实验表明，SMooGPT 在文本驱动的风格化动作生成方面表现出色，具有良好的可控性和泛化能力。

## 📝 摘要（中文）

风格化动作生成是计算机图形学中一个活跃的研究领域，尤其受益于扩散模型的快速发展。该任务旨在生成既尊重动作内容又符合期望风格的新动作，例如“像猴子一样绕圈行走”。现有研究试图通过动作风格迁移或条件动作生成来解决这个问题。它们通常将动作风格嵌入到潜在空间中，并在潜在空间中隐式地引导动作。尽管取得了一些进展，但这些方法存在可解释性和控制性低、对新风格的泛化能力有限以及由于公共风格化数据集中的强烈偏差而无法生成“行走”以外的动作等问题。本文基于以下观察，从推理-组合-生成的角度提出解决风格化动作生成问题：i) 人类动作通常可以用自然语言以身体部位为中心的方式有效地描述；ii) LLM 表现出强大的理解和推理人类动作的能力；iii) 人类动作具有内在的组合性质，可以通过有效的重组来促进新的动作内容或风格生成。因此，我们提出利用身体部位文本空间作为中间表示，并提出 SMooGPT，一个经过微调的 LLM，在生成所需的风格化动作时充当推理器、组合器和生成器。我们的方法在具有更高可解释性的身体部位文本空间中执行，从而实现细粒度的动作控制，有效解决动作内容和风格之间的潜在冲突，并且由于 LLM 的开放词汇能力而很好地推广到新风格。全面的实验和评估以及用户感知研究证明了我们方法的有效性，尤其是在纯文本驱动的风格化动作生成下。

## 🔬 方法详解

**问题定义**：现有风格化动作生成方法主要通过潜在空间操作实现，存在可解释性差、控制粒度粗、泛化能力弱等问题。特别是，现有方法严重依赖于“行走”等特定动作数据集，难以生成其他类型的风格化动作。

**核心思路**：论文的核心思路是将风格化动作生成问题分解为三个阶段：推理、组合和生成。利用大型语言模型（LLM）的强大能力，首先将动作分解为基于身体部位的文本描述，然后根据目标风格进行组合，最后生成最终的风格化动作。这种方法利用了 LLM 的开放词汇能力和对人类动作的理解能力，从而提高了可解释性和泛化能力。

**技术框架**：SMooGPT 的整体框架包含以下几个主要模块：1) 动作文本编码器：将输入的动作序列编码为文本描述，以身体部位为中心。2) LLM 推理器：利用微调的 LLM，根据输入的动作文本描述和目标风格，推理出新的身体部位动作描述。3) 动作文本解码器：将 LLM 生成的身体部位动作描述解码为最终的动作序列。整个流程在身体部位文本空间中进行，提高了可解释性和可控性。

**关键创新**：该论文最重要的创新点在于将大型语言模型引入风格化动作生成领域，并利用身体部位文本空间作为中间表示。这种方法打破了传统方法对潜在空间的依赖，提高了可解释性和可控性，并能够更好地泛化到新的风格和动作类型。

**关键设计**：SMooGPT 的关键设计包括：1) 身体部位文本编码方式：采用一种能够有效描述身体部位动作的文本编码方式，例如使用动词和形容词来描述身体部位的运动状态。2) LLM 微调策略：针对风格化动作生成任务，对 LLM 进行微调，使其能够更好地理解和推理人类动作。3) 损失函数设计：设计合适的损失函数，以保证生成的动作序列的流畅性和自然性。

## 📊 实验亮点

实验结果表明，SMooGPT 在风格化动作生成方面取得了显著的成果。与现有方法相比，SMooGPT 能够生成更具多样性和可控性的风格化动作，并且在纯文本驱动的风格化动作生成任务中表现出色。用户感知研究也表明，SMooGPT 生成的动作更符合人类的审美。

## 🎯 应用场景

SMooGPT 可应用于游戏开发、虚拟现实、动画制作等领域，例如，可以根据文本描述快速生成具有特定风格的角色动作，提高内容创作效率。此外，该方法还可以用于人机交互领域，例如，根据用户的语音指令生成相应的机器人动作。

## 📄 摘要（原文）

> Stylized motion generation is actively studied in computer graphics, especially benefiting from the rapid advances in diffusion models. The goal of this task is to produce a novel motion respecting both the motion content and the desired motion style, e.g., ``walking in a loop like a Monkey''. Existing research attempts to address this problem via motion style transfer or conditional motion generation. They typically embed the motion style into a latent space and guide the motion implicitly in a latent space as well. Despite the progress, their methods suffer from low interpretability and control, limited generalization to new styles, and fail to produce motions other than ``walking'' due to the strong bias in the public stylization dataset. In this paper, we propose to solve the stylized motion generation problem from a new perspective of reasoning-composition-generation, based on our observations: i) human motion can often be effectively described using natural language in a body-part centric manner, ii) LLMs exhibit a strong ability to understand and reason about human motion, and iii) human motion has an inherently compositional nature, facilitating the new motion content or style generation via effective recomposing. We thus propose utilizing body-part text space as an intermediate representation, and present SMooGPT, a fine-tuned LLM, acting as a reasoner, composer, and generator when generating the desired stylized motion. Our method executes in the body-part text space with much higher interpretability, enabling fine-grained motion control, effectively resolving potential conflicts between motion content and style, and generalizes well to new styles thanks to the open-vocabulary ability of LLMs. Comprehensive experiments and evaluations, and a user perceptual study, demonstrate the effectiveness of our approach, especially under the pure text-driven stylized motion generation.

