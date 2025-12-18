---
layout: default
title: Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models
---

# Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13237" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13237v1</a>
  <a href="https://arxiv.org/pdf/2510.13237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13237v1', 'Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haochuan Xu, Yun Sing Koh, Shuhuai Huang, Zirun Zhou, Di Wang, Jun Sakuma, Jingfeng Zhang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-15

**🔗 代码/项目**: [PROJECT_PAGE](https://edpa-attack.github.io/)

---

## 💡 一句话要点

**提出针对视觉-语言-动作模型的模型无关对抗攻击与防御方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `对抗攻击` `对抗防御` `模型无关` `机器人学习`

## 📋 核心要点

1. VLA模型在机器人学习中表现出色，但其对抗鲁棒性不足，容易受到攻击。
2. 提出嵌入扰动补丁攻击(EDPA)，通过扰乱视觉和文本的语义对齐来欺骗VLA模型。
3. 设计对抗微调防御机制，提升模型对对抗样本的鲁棒性，并在LIBERO基准上验证有效性。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在机器人学习领域取得了革命性的进展，使机器人能够根据自然语言指令执行复杂的物理任务。尽管取得了这些进展，但它们对抗攻击的鲁棒性仍未被充分探索。本文针对VLA模型，提出了对抗补丁攻击和相应的防御策略。我们首先介绍了嵌入扰动补丁攻击(EDPA)，这是一种模型无关的对抗攻击，可以直接将生成的补丁放置在摄像头的视野中。与先前的方法相比，EDPA可以很容易地应用于不同的VLA模型，而不需要事先了解模型架构或受控的机器人机械臂。EDPA通过(i)扰乱视觉和文本潜在表示之间的语义对齐，以及(ii)最大化对抗和相应的干净视觉输入之间潜在表示的差异来构建这些补丁。通过优化这些目标，EDPA扭曲了VLA对视觉信息的解释，导致模型重复生成不正确的动作，最终导致无法完成给定的机器人任务。为了应对这种情况，我们提出了一种针对视觉编码器的对抗微调方案，其中优化编码器，使其为干净的和对抗扰动的视觉输入生成相似的潜在表示。在广泛认可的LIBERO机器人仿真基准上的大量评估表明，EDPA大大提高了最先进的VLA模型的任务失败率，而我们提出的防御有效地缓解了这种退化。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作(VLA)模型在机器人控制任务中取得了显著进展，但它们容易受到对抗攻击的影响。特别是，如何在不了解模型内部结构的情况下，设计有效的对抗攻击方法，并提出相应的防御策略，是一个重要的挑战。现有的对抗攻击方法通常需要针对特定模型进行设计，泛化能力较差。

**核心思路**：本文的核心思路是设计一种模型无关的对抗补丁攻击(EDPA)，通过扰乱视觉和文本嵌入之间的语义对齐，使得VLA模型对视觉信息的理解产生偏差，从而导致错误的动作输出。同时，提出一种对抗微调策略，通过让模型学习对对抗样本具有鲁棒性的特征表示，来提高模型的防御能力。

**技术框架**：EDPA攻击框架主要包括两个目标：一是扰乱视觉和文本潜在表示之间的语义对齐，二是最大化对抗样本和干净样本在潜在表示上的差异。防御框架则采用对抗微调的方式，通过最小化干净样本和对抗样本在视觉编码器输出的潜在表示之间的距离，来提高模型的鲁棒性。整体流程为：首先使用EDPA生成对抗补丁，然后将补丁添加到输入图像中，再将带有补丁的图像输入到VLA模型中，观察模型的行为。为了防御攻击，使用对抗微调策略训练视觉编码器。

**关键创新**：EDPA的关键创新在于其模型无关性，它不需要了解VLA模型的具体架构，就可以有效地攻击模型。此外，通过直接在图像空间中添加补丁，使得攻击更具实际意义。对抗微调防御策略能够有效地提高模型对EDPA攻击的鲁棒性。

**关键设计**：EDPA攻击的关键设计包括：(1) 语义对齐损失：用于衡量视觉和文本嵌入之间的相似度，通过最小化该损失来扰乱语义对齐。(2) 差异最大化损失：用于最大化对抗样本和干净样本在潜在表示上的差异，使得攻击更加有效。对抗微调防御的关键设计在于：(1) 对抗训练数据生成：使用EDPA生成对抗样本。(2) 损失函数：最小化干净样本和对抗样本在视觉编码器输出的潜在表示之间的距离。

## 📊 实验亮点

实验结果表明，EDPA攻击能够显著提高最先进VLA模型的任务失败率。在LIBERO基准测试中，EDPA攻击使得VLA模型的任务成功率大幅下降。同时，提出的对抗微调防御策略能够有效地缓解这种性能下降，显著提高模型对EDPA攻击的鲁棒性。具体性能数据在论文中详细展示。

## 🎯 应用场景

该研究成果可应用于提升机器人系统的安全性和可靠性，尤其是在需要与人类交互或在复杂环境中执行任务的场景中。例如，在自动驾驶、智能制造、医疗机器人等领域，提高VLA模型对抗恶意攻击的鲁棒性至关重要。未来的研究可以进一步探索更高效的防御策略，以及更具隐蔽性的攻击方法。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have achieved revolutionary progress in robot learning, enabling robots to execute complex physical robot tasks from natural language instructions. Despite this progress, their adversarial robustness remains underexplored. In this work, we propose both adversarial patch attack and corresponding defense strategies for VLA models. We first introduce the Embedding Disruption Patch Attack (EDPA), a model-agnostic adversarial attack that generates patches directly placeable within the camera's view. In comparison to prior methods, EDPA can be readily applied to different VLA models without requiring prior knowledge of the model architecture, or the controlled robotic manipulator. EDPA constructs these patches by (i) disrupting the semantic alignment between visual and textual latent representations, and (ii) maximizing the discrepancy of latent representations between adversarial and corresponding clean visual inputs. Through the optimization of these objectives, EDPA distorts the VLA's interpretation of visual information, causing the model to repeatedly generate incorrect actions and ultimately result in failure to complete the given robotic task. To counter this, we propose an adversarial fine-tuning scheme for the visual encoder, in which the encoder is optimized to produce similar latent representations for both clean and adversarially perturbed visual inputs. Extensive evaluations on the widely recognized LIBERO robotic simulation benchmark demonstrate that EDPA substantially increases the task failure rate of cutting-edge VLA models, while our proposed defense effectively mitigates this degradation. The codebase is accessible via the homepage at https://edpa-attack.github.io/.

