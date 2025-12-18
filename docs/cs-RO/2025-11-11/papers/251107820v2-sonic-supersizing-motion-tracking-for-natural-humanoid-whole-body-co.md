---
layout: default
title: SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
---

# SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07820" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07820v2</a>
  <a href="https://arxiv.org/pdf/2511.07820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07820v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.07820v2', 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyi Luo, Ye Yuan, Tingwu Wang, Chenran Li, Sirui Chen, Fernando Castañeda, Zi-Ang Cao, Jiefeng Li, David Minor, Qingwei Ben, Xingye Da, Runyu Ding, Cyrus Hogg, Lina Song, Edy Lim, Eugene Jeong, Tairan He, Haoru Xue, Wenli Xiao, Zi Wang, Simon Yuen, Jan Kautz, Yan Chang, Umar Iqbal, Linxi "Jim" Fan, Yuke Zhu

**分类**: cs.RO, cs.AI, cs.CV, cs.GR, eess.SY

**发布日期**: 2025-11-11 (更新: 2025-12-04)

**备注**: Project page: https://nvlabs.github.io/SONIC/

---

## 💡 一句话要点

**SONIC：通过大规模运动跟踪实现自然的人形全身控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人控制` `运动跟踪` `大规模学习` `Transformer` `运动捕捉` `全身运动` `通用控制器`

## 📋 核心要点

1. 现有的人形机器人神经控制器规模较小，行为集有限，训练耗时，难以充分利用大规模数据和算力。
2. 论文提出将运动跟踪作为人形机器人控制的基础任务，通过大规模数据和算力训练通用控制器，无需手动设计奖励函数。
3. 实验表明，该方法在运动跟踪任务上表现出良好的扩展性，性能随数据和算力增加而提升，并能泛化到未见过的运动。

## 📝 摘要（中文）

本文提出了一种通用人形机器人控制器，通过扩展模型容量、数据量和计算资源，实现了自然且鲁棒的全身运动控制。论文将运动跟踪视为人形机器人控制的一个自然且可扩展的任务，利用来自多样化运动捕捉数据的密集监督，无需手动设计奖励函数即可获取人类运动先验知识。通过扩展网络规模（从120万到4200万参数）、数据集大小（超过1亿帧，700小时高质量运动数据）和计算资源（9000 GPU小时），构建了一个用于运动跟踪的基础模型。该模型通过实时通用运动学规划器将运动跟踪连接到下游任务执行，实现自然和交互式控制，并使用统一的token空间支持各种运动输入接口，如VR遥操作设备、人类视频和视觉-语言-动作（VLA）模型。实验表明，大规模运动跟踪具有良好的特性：性能随着计算资源和数据多样性的增加而稳步提高，并且学习到的表示可以泛化到未见过的运动，从而为人形机器人控制奠定了坚实的基础。

## 🔬 方法详解

**问题定义**：现有的人形机器人控制方法，特别是基于强化学习的方法，通常需要手动设计复杂的奖励函数，并且难以泛化到不同的任务和环境。此外，现有模型的规模和训练数据量相对较小，限制了其性能和泛化能力。因此，如何利用大规模数据和算力，构建一个通用且鲁棒的人形机器人控制器是一个关键问题。

**核心思路**：论文的核心思路是将运动跟踪作为人形机器人控制的一个基础任务。通过学习人类运动的先验知识，机器人可以更好地理解和模仿人类的动作，从而实现更自然和鲁棒的控制。这种方法避免了手动设计奖励函数的复杂性，并且可以利用大规模的运动捕捉数据进行训练。

**技术框架**：该方法构建了一个用于运动跟踪的基础模型，该模型通过扩展网络规模、数据集大小和计算资源进行训练。整体架构包含三个主要部分：1) 运动捕捉数据预处理，将原始数据转换为模型可以处理的格式；2) 运动跟踪模型训练，使用大规模数据训练模型，使其能够准确地跟踪人类运动；3) 运动规划和控制，利用训练好的模型进行运动规划和控制，实现人形机器人的全身运动。

**关键创新**：最重要的技术创新点在于将运动跟踪作为人形机器人控制的基础任务，并利用大规模数据和算力进行训练。这种方法避免了手动设计奖励函数的复杂性，并且可以学习到更丰富的运动先验知识。此外，该方法还提出了一个统一的token空间，可以支持各种运动输入接口，如VR遥操作设备、人类视频和视觉-语言-动作（VLA）模型。

**关键设计**：论文中使用了Transformer架构作为运动跟踪模型的基础。损失函数主要包括运动学损失和动力学损失，用于约束模型的输出。网络规模从120万到4200万参数不等，数据集大小超过1亿帧，计算资源达到9000 GPU小时。此外，论文还设计了一个实时通用运动学规划器，用于将运动跟踪连接到下游任务执行。

## 📊 实验亮点

该研究通过扩展模型规模、数据量和计算资源，在运动跟踪任务上取得了显著的性能提升。实验结果表明，该方法可以准确地跟踪人类运动，并且能够泛化到未见过的运动。此外，该方法还能够支持各种运动输入接口，如VR遥操作设备、人类视频和视觉-语言-动作（VLA）模型。与现有方法相比，该方法具有更高的精度和更好的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种人形机器人控制场景，如家庭服务、医疗康复、工业自动化等。通过学习人类运动的先验知识，机器人可以更好地理解和模仿人类的动作，从而实现更自然和鲁棒的控制。此外，该方法还可以用于虚拟现实和增强现实等领域，为用户提供更逼真的交互体验。未来，该研究有望推动人形机器人技术的发展，使其能够更好地服务于人类社会。

## 📄 摘要（原文）

> Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs over several days. We show that scaling up model capacity, data, and compute yields a generalist humanoid controller capable of creating natural and robust whole-body movements. Specifically, we posit motion tracking as a natural and scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (from 1.2M to 42M parameters), dataset volume (over 100M frames, 700 hours of high-quality motion data), and compute (9k GPU hours). Beyond demonstrating the benefits of scale, we show the practical utility of our model through two mechanisms: (1) a real-time universal kinematic planner that bridges motion tracking to downstream task execution, enabling natural and interactive control, and (2) a unified token space that supports various motion input interfaces, such as VR teleoperation devices, human videos, and vision-language-action (VLA) models, all using the same policy. Scaling motion tracking exhibits favorable properties: performance improves steadily with increased compute and data diversity, and learned representations generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

