---
layout: default
title: WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control
---

# WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control

**arXiv**: [2512.11047v2](https://arxiv.org/abs/2512.11047) | [PDF](https://arxiv.org/pdf/2512.11047.pdf)

**作者**: Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe Suo, Chuang Wang, Zhihui Peng, Hongyang Li

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-12-11 (更新: 2025-12-15)

---

## 💡 一句话要点

**提出WholeBodyVLA，实现基于统一隐空间VLA的大范围全身Loco-Manipulation控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `Loco-Manipulation` `视觉语言动作` `强化学习` `隐空间学习`

## 📋 核心要点

1. 现有方法在操作感知的运动控制方面不足，限制了人形机器人在大范围场景下的Loco-Manipulation能力。
2. 提出WholeBodyVLA框架，利用统一隐空间学习VLA系统，从无动作视频中学习，并结合LMO-RL策略提升运动精度。
3. 在AgiBot X2上实验验证，WholeBodyVLA性能超越基线21.3%，展现出良好的泛化性和可扩展性。

## 📝 摘要（中文）

人形机器人需要精确的运动和灵巧的操作来执行具有挑战性的Loco-Manipulation任务。然而，现有的模块化或端到端方法在操作感知的运动方面存在不足，这限制了机器人的工作空间，阻碍了其执行大范围的Loco-Manipulation任务。我们认为这是由于：(1)缺乏人形遥操作数据导致难以获取Loco-Manipulation知识；(2)现有RL控制器的精度和稳定性有限，导致难以忠实可靠地执行运动命令。为了获取更丰富的Loco-Manipulation知识，我们提出了一个统一的隐空间学习框架，使视觉-语言-动作(VLA)系统能够从低成本的无动作自我中心视频中学习。此外，我们设计了一个高效的人工数据收集流程来扩充数据集并扩大收益。为了更精确地执行所需的运动命令，我们提出了一个专门为精确和稳定的核心Loco-Manipulation运动（如前进、转弯和下蹲）量身定制的面向Loco-Manipulation(LMO)的RL策略。基于这些组件，我们推出了WholeBodyVLA，一个用于人形Loco-Manipulation的统一框架。据我们所知，WholeBodyVLA是同类产品中首个实现大范围人形Loco-Manipulation的框架。通过在AgiBot X2人形机器人上的全面实验验证，其性能优于之前的基线21.3%，并且在广泛的任务中表现出强大的泛化能力和高度的可扩展性。

## 🔬 方法详解

**问题定义**：现有的人形机器人Loco-Manipulation方法，无论是模块化还是端到端，都缺乏对操作的感知，导致机器人难以在较大的空间范围内完成复杂的任务。主要痛点在于缺乏高质量的训练数据，以及现有强化学习控制器在运动控制方面的精度和稳定性不足。

**核心思路**：论文的核心思路是构建一个统一的隐空间学习框架，使机器人能够从低成本的、无动作的自我中心视频中学习Loco-Manipulation知识。同时，设计一个面向Loco-Manipulation的强化学习策略，以提高运动控制的精度和稳定性。通过结合视觉、语言和动作信息，实现更智能、更灵活的全身控制。

**技术框架**：WholeBodyVLA框架主要包含两个核心模块：一是基于视觉-语言-动作(VLA)的隐空间学习模块，用于从无动作视频中学习Loco-Manipulation知识；二是面向Loco-Manipulation(LMO)的强化学习策略，用于精确控制机器人的运动。整个流程包括数据收集、隐空间学习、策略训练和运动控制四个阶段。

**关键创新**：论文的关键创新在于提出了一个统一的隐空间学习框架，能够从低成本的无动作视频中学习Loco-Manipulation知识，从而克服了数据稀缺的问题。此外，LMO-RL策略的设计也针对性地提高了运动控制的精度和稳定性。

**关键设计**：VLA模块使用自编码器结构学习视觉和语言信息的联合隐空间表示。LMO-RL策略采用Actor-Critic架构，奖励函数的设计侧重于运动的精确性和稳定性，例如，对前进、转弯和下蹲等核心动作进行精细的奖励塑造。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，WholeBodyVLA在AgiBot X2人形机器人上的性能优于之前的基线21.3%。此外，该框架在不同的任务中表现出强大的泛化能力和高度的可扩展性，证明了其在实际应用中的潜力。这些结果验证了所提出方法的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于人形机器人在复杂环境下的自主操作，例如家庭服务、物流配送、灾难救援等。通过学习人类的动作和行为模式，机器人能够更好地理解环境，执行各种任务，提高工作效率和安全性。未来，该技术有望推动人形机器人在更广泛领域的应用。

## 📄 摘要（原文）

> Humanoid robots require precise locomotion and dexterous manipulation to perform challenging loco-manipulation tasks. Yet existing approaches, modular or end-to-end, are deficient in manipulation-aware locomotion. This confines the robot to a limited workspace, preventing it from performing large-space loco-manipulation. We attribute this to: (1) the challenge of acquiring loco-manipulation knowledge due to the scarcity of humanoid teleoperation data, and (2) the difficulty of faithfully and reliably executing locomotion commands, stemming from the limited precision and stability of existing RL controllers. To acquire richer loco-manipulation knowledge, we propose a unified latent learning framework that enables Vision-Language-Action (VLA) system to learn from low-cost action-free egocentric videos. Moreover, an efficient human data collection pipeline is devised to augment the dataset and scale the benefits. To execute the desired locomotion commands more precisely, we present a loco-manipulation-oriented (LMO) RL policy specifically tailored for accurate and stable core loco-manipulation movements, such as advancing, turning, and squatting. Building on these components, we introduce WholeBodyVLA, a unified framework for humanoid loco-manipulation. To the best of our knowledge, WholeBodyVLA is one of its kind enabling large-space humanoid loco-manipulation. It is verified via comprehensive experiments on the AgiBot X2 humanoid, outperforming prior baseline by 21.3%. It also demonstrates strong generalization and high extensibility across a broad range of tasks.

