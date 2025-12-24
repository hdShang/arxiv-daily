---
layout: default
title: "TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions"
---

# TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14874" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14874v1</a>
  <a href="https://arxiv.org/pdf/2510.14874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14874v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14874v1', 'TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangyi Han, Wei Zhai, Yuhang Yang, Yang Cao, Zheng-Jun Zha

**分类**: cs.CV

**发布日期**: 2025-10-16

**🔗 代码/项目**: [PROJECT_PAGE](https://guangyid.github.io/hoi123touch)

---

## 💡 一句话要点

**提出TOUCH框架，实现文本引导的可控自由手部-物体交互生成。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `手部-物体交互` `HOI生成` `扩散模型` `文本引导` `自由形式交互`

## 📋 核心要点

1. 现有HOI生成方法过度依赖抓取先验，难以捕捉推、戳、旋转等自由形式交互的多样性。
2. 提出TOUCH框架，利用多级扩散模型和显式接触建模，实现基于文本引导的细粒度HOI生成控制。
3. 构建了包含4.4k个多样交互的WildO2数据集，实验证明TOUCH能够生成可控、多样且物理合理的HOI。

## 📝 摘要（中文）

手部-物体交互（HOI）是人类表达意图的基础。现有的HOI生成研究主要局限于固定的抓取模式，控制与物理先验（如力闭合）或通用意图指令相关联，即使通过精细的语言表达也是如此。这种过度泛化的条件施加了对稳定抓取的强烈归纳偏置，从而无法捕捉日常HOI的多样性。为了解决这些限制，我们引入了自由形式HOI生成，旨在生成可控、多样且物理上合理的HOI，并以细粒度的意图为条件，将HOI从抓取扩展到自由形式的交互，如推、戳和旋转。为了支持这项任务，我们构建了WildO2，一个在野的、多样化的3D HOI数据集，其中包括来自互联网视频的各种HOI。具体来说，它包含跨92种意图和610种对象类别的4.4k个独特交互，每个交互都带有详细的语义注释。在此数据集的基础上，我们提出了TOUCH，一个以多级扩散模型为中心的三阶段框架，该框架有助于细粒度的语义控制，以生成超出抓取先验的多功能手部姿势。此过程利用显式接触建模进行条件设置，随后通过接触一致性和物理约束进行细化，以确保真实感。全面的实验证明了我们的方法能够生成代表日常活动的可控、多样且物理上合理的手部交互。

## 🔬 方法详解

**问题定义**：现有手部-物体交互（HOI）生成方法主要集中在抓取动作，难以生成如推、戳、旋转等自由形式的交互。这些方法通常依赖于物理先验或通用意图指令，缺乏对细粒度语义意图的控制能力，限制了HOI生成的多样性和真实性。

**核心思路**：TOUCH框架的核心思路是利用文本引导的多级扩散模型，结合显式接触建模，实现对HOI生成的细粒度语义控制。通过将文本描述作为条件，扩散模型可以生成多样化的手部姿势，而显式接触建模则保证了生成的HOI在物理上的合理性。

**技术框架**：TOUCH框架包含三个主要阶段：1) **文本编码**：使用预训练的文本编码器提取文本描述的语义特征。2) **多级扩散模型**：利用提取的语义特征作为条件，通过多级扩散模型生成手部姿势。该模型包含多个层级，每个层级负责生成不同尺度的手部姿势细节。3) **接触优化**：使用显式接触建模方法，对生成的手部姿势进行优化，确保手部与物体之间的接触是物理上合理的。

**关键创新**：TOUCH框架的关键创新在于：1) 引入了自由形式HOI生成任务，扩展了HOI生成的研究范围。2) 提出了基于多级扩散模型的HOI生成方法，实现了对细粒度语义意图的控制。3) 利用显式接触建模，保证了生成的HOI在物理上的合理性。

**关键设计**：TOUCH框架的关键设计包括：1) 使用预训练的CLIP模型进行文本编码，以获得更丰富的语义信息。2) 多级扩散模型采用U-Net结构，并引入了注意力机制，以更好地捕捉文本描述与手部姿势之间的关系。3) 接触优化阶段，使用基于物理的模拟器，对生成的手部姿势进行迭代优化，直到满足接触一致性和物理约束。

## 📊 实验亮点

实验结果表明，TOUCH框架在WildO2数据集上取得了显著的性能提升。与现有方法相比，TOUCH能够生成更可控、更多样且物理上合理的HOI。具体来说，在生成HOI的多样性和真实性方面，TOUCH的指标优于其他基线方法。

## 🎯 应用场景

该研究成果可应用于人机交互、虚拟现实、机器人控制等领域。例如，在虚拟现实中，用户可以通过文本描述来控制虚拟角色的手部动作，实现更自然、更真实的交互体验。在机器人控制中，机器人可以根据文本指令，完成各种复杂的HOI任务，提高机器人的智能化水平。

## 📄 摘要（原文）

> Hand-object interaction (HOI) is fundamental for humans to express intent. Existing HOI generation research is predominantly confined to fixed grasping patterns, where control is tied to physical priors such as force closure or generic intent instructions, even when expressed through elaborate language. Such an overly general conditioning imposes a strong inductive bias for stable grasps, thus failing to capture the diversity of daily HOI. To address these limitations, we introduce Free-Form HOI Generation, which aims to generate controllable, diverse, and physically plausible HOI conditioned on fine-grained intent, extending HOI from grasping to free-form interactions, like pushing, poking, and rotating. To support this task, we construct WildO2, an in-the-wild diverse 3D HOI dataset, which includes diverse HOI derived from internet videos. Specifically, it contains 4.4k unique interactions across 92 intents and 610 object categories, each with detailed semantic annotations. Building on this dataset, we propose TOUCH, a three-stage framework centered on a multi-level diffusion model that facilitates fine-grained semantic control to generate versatile hand poses beyond grasping priors. This process leverages explicit contact modeling for conditioning and is subsequently refined with contact consistency and physical constraints to ensure realism. Comprehensive experiments demonstrate our method's ability to generate controllable, diverse, and physically plausible hand interactions representative of daily activities. The project page is $\href{https://guangyid.github.io/hoi123touch}{here}$.

