---
layout: default
title: "Towards Closed-Loop Embodied Empathy Evolution: Probing LLM-Centric Lifelong Empathic Motion Generation in Unseen Scenarios"
---

# Towards Closed-Loop Embodied Empathy Evolution: Probing LLM-Centric Lifelong Empathic Motion Generation in Unseen Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19551" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19551v1</a>
  <a href="https://arxiv.org/pdf/2512.19551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19551v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19551v1', 'Towards Closed-Loop Embodied Empathy Evolution: Probing LLM-Centric Lifelong Empathic Motion Generation in Unseen Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiawen Wang, Jingjing Wang Tianyang Chen, Min Zhang, Guodong Zhou

**分类**: cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出基于LLM的终身情感动作生成框架，解决新场景下的情感动作泛化问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `情感动作生成` `终身学习` `大型语言模型` `混合专家模型` `具身智能` `情感解耦` `场景适应`

## 📋 核心要点

1. 现有情感动作生成方法主要关注在单一固定数据集上的性能提升，忽略了灵活且规模增长的运动场景。
2. 论文提出基于LLM的终身情感动作生成任务，并设计情感可迁移和场景自适应的混合专家模型(ES-MoE)。
3. 实验结果表明，ES-MoE在多个L^2-EMG数据集上优于现有先进基线方法，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种新的基于LLM的终身情感动作生成(L^2-EMG)任务，旨在使LLM能够持续获取不同未见场景下的情感动作生成知识，从而有助于构建一个具备同理心和智能的闭环和自我进化的具身智能体。本文提出了L^2-EMG任务中的两个关键挑战，即情感解耦挑战和场景适应挑战。为此，本文提出了一种情感可迁移和场景自适应的混合专家模型(ES-MoE)，该模型设计了一个因果引导的情感解耦块和一个场景自适应的专家构建块，分别应对这两个挑战。特别地，本文构建了多个L^2-EMG数据集来验证ES-MoE方法的有效性。广泛的评估表明，ES-MoE优于先进的基线方法。

## 🔬 方法详解

**问题定义**：现有的人类中心情感动作生成方法主要关注在单个数据集上的性能提升，缺乏在新兴的、规模不断增长的运动场景（如体育、舞蹈）中的泛化能力。这些新场景的学习对于提升模型在真实世界的泛化能力至关重要。因此，需要一种方法能够使模型持续学习不同场景下的情感动作生成知识。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的知识和推理能力，使其能够像人类一样，通过不断学习新的场景和情感表达方式，从而具备终身学习情感动作生成的能力。通过设计特定的模块来解决情感解耦和场景适应的挑战，使得模型能够更好地理解和生成情感化的动作。

**技术框架**：整体框架是一个基于LLM的混合专家模型（ES-MoE）。主要包含两个核心模块：1) 因果引导的情感解耦块：用于将情感信息从动作中分离出来，使得模型可以更好地理解和控制情感的表达。2) 场景自适应的专家构建块：用于根据不同的场景选择合适的专家模型，从而实现场景自适应的动作生成。整个流程包括：输入文本描述，情感解耦，场景选择，动作生成，以及通过损失函数进行优化。

**关键创新**：论文的关键创新在于提出了一个基于LLM的终身情感动作生成框架，并设计了情感可迁移和场景自适应的混合专家模型（ES-MoE）。ES-MoE能够有效地解决情感解耦和场景适应的挑战，使得模型可以在不同的未见场景下生成情感化的动作。与现有方法相比，该方法更具泛化能力和可扩展性。

**关键设计**：情感解耦块采用因果推理的方式，通过干预情感变量来学习情感和动作之间的因果关系。场景自适应的专家构建块通过学习不同场景的特征表示，并根据场景特征选择合适的专家模型。损失函数包括动作生成损失、情感一致性损失和场景适应损失，用于优化模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19551v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19551v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19551v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ES-MoE在多个L^2-EMG数据集上进行了广泛的评估，实验结果表明，ES-MoE在动作生成质量和情感表达准确性方面均优于现有先进的基线方法。具体性能提升数据未知，但论文强调ES-MoE在未见场景下的泛化能力显著增强。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏、人机交互等领域，例如创建更具情感表达能力的虚拟角色，或者使机器人能够根据人类的情感状态做出相应的动作反应。此外，该技术还可以用于辅助情感障碍患者的康复治疗，帮助他们更好地理解和表达情感。

## 📄 摘要（原文）

> In the literature, existing human-centric emotional motion generation methods primarily focus on boosting performance within a single scale-fixed dataset, largely neglecting the flexible and scale-increasing motion scenarios (e.g., sports, dance), whereas effectively learning these newly emerging scenarios can significantly enhance the model's real-world generalization ability. Inspired by this, this paper proposes a new LLM-Centric Lifelong Empathic Motion Generation (L^2-EMG) task, which aims to equip LLMs with the capability to continually acquire emotional motion generation knowledge across different unseen scenarios, potentially contributing to building a closed-loop and self-evolving embodied agent equipped with both empathy and intelligence. Further, this paper poses two key challenges in the L^2-EMG task, i.e., the emotion decoupling challenge and the scenario adapting challenge. To this end, this paper proposes an Emotion-Transferable and Scenario-Adapted Mixture of Experts (ES-MoE) approach which designs a causal-guided emotion decoupling block and a scenario-adapted expert constructing block to address the two challenges, respectively. Especially, this paper constructs multiple L^2-EMG datasets to validate the effectiveness of the ES-MoE approach. Extensive evaluations show that ES-MoE outperforms advanced baselines.

