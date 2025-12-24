---
layout: default
title: "DINOv3-Diffusion Policy: Self-Supervised Large Visual Model for Visuomotor Diffusion Policy Learning"
---

# DINOv3-Diffusion Policy: Self-Supervised Large Visual Model for Visuomotor Diffusion Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17684" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17684v1</a>
  <a href="https://arxiv.org/pdf/2509.17684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17684v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17684v1', 'DINOv3-Diffusion Policy: Self-Supervised Large Visual Model for Visuomotor Diffusion Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: ThankGod Egbe, Peng Wang, Zhihao Guo, Zidong Chen

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-22

---

## 💡 一句话要点

**DINOv3赋能扩散策略：用于机器人视觉运动策略学习的自监督大型视觉模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `视觉运动策略` `扩散策略` `自监督学习` `DINOv3` `视觉编码器` `迁移学习`

## 📋 核心要点

1. 现有机器人操作任务依赖ImageNet预训练模型，但其领域差异限制了性能和泛化能力。
2. 论文提出利用自监督学习的DINOv3作为视觉编码器，探索其在视觉运动扩散策略学习中的潜力。
3. 实验表明，微调的DINOv3在多个任务上超越ResNet-18，且冻结的DINOv3也表现出竞争力。

## 📝 摘要（中文）

本文评估了DINOv3，一种最新的大规模自监督视觉骨干网络，在机器人操作中的视觉运动扩散策略学习方面的性能。我们研究了在三种训练模式下：从头开始训练、冻结和微调，纯自监督编码器是否能与传统的监督ImageNet预训练骨干网络（例如，ResNet-18）相媲美或超越。在四个基准任务（Push-T、Lift、Can、Square）中使用统一的FiLM条件扩散策略，我们发现：（i）微调后的DINOv3在多个任务上与ResNet-18相匹配或超过；（ii）冻结的DINOv3仍然具有竞争力，表明其具有强大的可迁移先验知识；（iii）自监督特征提高了样本效率和鲁棒性。这些结果支持自监督大型视觉模型作为动作扩散策略的有效、可泛化的感知前端，从而推动了在机器人操作中对可扩展的无标签预训练的进一步探索。与使用ResNet18作为骨干网络相比，我们使用DINOv3的方法在Can等具有挑战性的任务中，测试时的成功率绝对提高了10%，并且在Lift、PushT和Square等任务中表现相当。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作任务中，现有方法依赖ImageNet预训练模型导致的领域泛化性不足的问题。ImageNet预训练模型与机器人操作环境存在显著差异，限制了策略的学习效率和鲁棒性。

**核心思路**：论文的核心思路是利用大规模自监督学习得到的DINOv3模型作为视觉编码器，替代传统的ImageNet预训练模型。DINOv3通过自监督学习，能够学习到更通用的视觉特征，从而更好地适应机器人操作环境。这样设计的目的是为了提高策略的学习效率、泛化能力和鲁棒性。

**技术框架**：整体框架包含一个视觉编码器（DINOv3或ResNet-18）和一个FiLM条件扩散策略。视觉编码器将图像输入转换为特征向量，然后将特征向量输入到FiLM条件扩散策略中，生成动作。训练过程中，比较真实动作和预测动作之间的差异，更新策略参数。论文在三种模式下评估DINOv3：从头开始训练、冻结和微调。

**关键创新**：最重要的技术创新点在于将大规模自监督学习得到的DINOv3模型应用于机器人视觉运动策略学习。与传统的监督学习方法相比，自监督学习能够利用大量的无标签数据，学习到更通用的视觉特征。此外，论文还探索了DINOv3在不同训练模式下的性能，为实际应用提供了指导。

**关键设计**：论文使用FiLM条件扩散策略，该策略能够根据视觉特征动态调整扩散过程。损失函数采用均方误差（MSE）来衡量预测动作和真实动作之间的差异。实验中，作者使用了四个基准任务（Push-T、Lift、Can、Square）来评估不同模型的性能。DINOv3模型采用ViT架构，并使用大规模无标签图像数据进行预训练。

## 📊 实验亮点

实验结果表明，在Can任务中，使用微调后的DINOv3作为视觉编码器，测试时的成功率比使用ResNet-18提高了10%。在Lift、PushT和Square等任务中，DINOv3的性能与ResNet-18相当。此外，冻结的DINOv3也表现出竞争力，表明其具有强大的可迁移先验知识。这些结果验证了自监督学习在机器人视觉运动策略学习中的有效性。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如物体抓取、装配、导航等。通过使用自监督学习得到的视觉模型，可以降低对大量标注数据的依赖，提高机器人在复杂环境中的适应性和泛化能力。未来，该方法有望推动机器人技术在工业自动化、医疗健康、家庭服务等领域的广泛应用。

## 📄 摘要（原文）

> This paper evaluates DINOv3, a recent large-scale self-supervised vision backbone, for visuomotor diffusion policy learning in robotic manipulation. We investigate whether a purely self-supervised encoder can match or surpass conventional supervised ImageNet-pretrained backbones (e.g., ResNet-18) under three regimes: training from scratch, frozen, and finetuned. Across four benchmark tasks (Push-T, Lift, Can, Square) using a unified FiLM-conditioned diffusion policy, we find that (i) finetuned DINOv3 matches or exceeds ResNet-18 on several tasks, (ii) frozen DINOv3 remains competitive, indicating strong transferable priors, and (iii) self-supervised features improve sample efficiency and robustness. These results support self-supervised large visual models as effective, generalizable perceptual front-ends for action diffusion policies, motivating further exploration of scalable label-free pretraining in robotic manipulation. Compared to using ResNet18 as a backbone, our approach with DINOv3 achieves up to a 10% absolute increase in test-time success rates on challenging tasks such as Can, and on-the-par performance in tasks like Lift, PushT, and Square.

