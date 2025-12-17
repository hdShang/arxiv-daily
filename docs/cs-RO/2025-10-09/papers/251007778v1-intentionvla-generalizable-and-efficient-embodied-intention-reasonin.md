---
layout: default
title: IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction
---

# IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07778" target="_blank" class="toolbar-btn">arXiv: 2510.07778v1</a>
    <a href="https://arxiv.org/pdf/2510.07778.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07778v1" 
            onclick="toggleFavorite(this, '2510.07778v1', 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yandu Chen, Kefan Gu, Yuqing Wen, Yucheng Zhao, Tiancai Wang, Liqiang Nie

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**IntentionVLA：面向人机交互的可泛化高效具身意图推理框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `具身智能` `意图推理` `视觉语言动作模型` `课程学习`

## 📋 核心要点

1. 现有VLA模型缺乏推理密集型预训练和推理引导的操作，难以进行复杂真实世界交互所需的隐式人类意图推理。
2. IntentionVLA通过课程学习范式和高效推理机制，利用推理数据赋予模型推理和感知能力，并使用推理输出指导动作生成。
3. 实验表明，IntentionVLA在直接和意图指令下均显著优于现有模型，并在分布外意图任务和零样本人机交互中表现出色。

## 📝 摘要（中文）

本文提出IntentionVLA，一个具有课程学习范式和高效推理机制的VLA框架，旨在解决现有VLA模型在复杂真实世界交互中进行隐式人类意图推理能力不足的问题。IntentionVLA首先利用精心设计的推理数据，结合意图推断、空间定位和紧凑的具身推理，赋予模型推理和感知能力。在后续的微调阶段，IntentionVLA采用紧凑的推理输出作为动作生成的上下文指导，从而在间接指令下实现快速推理。实验结果表明，IntentionVLA显著优于$π_0$，在直接指令下的成功率提高了18％，在意图指令下比ECoT高出28％。在分布外的意图任务上，IntentionVLA的成功率是所有基线的两倍以上，并进一步实现了40％成功率的零样本人机交互。这些结果表明IntentionVLA是下一代人机交互系统的有希望的范例。

## 🔬 方法详解

**问题定义**：现有Vision-Language-Action (VLA)模型主要在与具身场景相关性有限的多模态任务上进行预训练，然后微调以将显式指令映射到动作。这导致模型缺乏足够的推理能力，无法处理需要理解人类隐式意图的复杂人机交互任务。现有方法的痛点在于无法有效结合感知和推理，尤其是在处理间接指令时。

**核心思路**：IntentionVLA的核心思路是通过课程学习的方式，首先让模型学习进行意图推理，空间定位和紧凑的具身推理，从而赋予模型推理和感知能力。然后，在微调阶段，利用这些推理结果作为上下文信息，指导动作的生成。这样，模型就可以在间接指令下进行快速且准确的推理。

**技术框架**：IntentionVLA包含预训练和微调两个主要阶段。在预训练阶段，模型使用精心设计的推理数据集进行训练，该数据集包含意图推断、空间定位和紧凑的具身推理等任务。在微调阶段，模型使用具身任务的数据集进行微调，同时将预训练阶段的推理结果作为上下文信息输入到模型中，指导动作的生成。整体流程是从视觉和语言输入开始，经过意图推理模块，生成紧凑的推理表示，最后通过动作生成模块输出控制指令。

**关键创新**：IntentionVLA的关键创新在于其课程学习范式和高效推理机制。通过课程学习，模型可以逐步学习从简单到复杂的推理任务，从而提高模型的泛化能力。同时，通过将推理结果作为上下文信息，模型可以更有效地利用感知信息，从而提高推理的准确性和效率。与现有方法相比，IntentionVLA更注重模型的推理能力，尤其是在处理隐式意图时的推理能力。

**关键设计**：IntentionVLA的关键设计包括推理数据集的设计和推理结果的表示方式。推理数据集需要包含各种意图推断、空间定位和具身推理的场景，以覆盖不同的推理需求。推理结果采用紧凑的表示方式，例如使用符号或向量来表示意图、位置和动作等信息。具体的损失函数包括用于意图分类的交叉熵损失、用于空间定位的回归损失和用于动作生成的序列预测损失。网络结构方面，可以使用Transformer等模型来处理视觉和语言输入，并使用专门的推理模块来生成推理结果。

## 📊 实验亮点

实验结果表明，IntentionVLA在直接指令下的成功率比$π_0$高出18％，在意图指令下比ECoT高出28％。在分布外的意图任务上，IntentionVLA的成功率是所有基线的两倍以上，并实现了40％成功率的零样本人机交互。这些数据表明，IntentionVLA在各种人机交互任务中都具有显著的优势。

## 🎯 应用场景

IntentionVLA可应用于各种人机交互场景，例如家庭服务机器人、医疗辅助机器人和工业协作机器人。该技术能够使机器人更好地理解人类的意图，从而更安全、更有效地与人类进行协作。未来，IntentionVLA有望成为下一代人机交互系统的核心技术，推动人机协作向更智能、更自然的方向发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models leverage pretrained vision-language models (VLMs) to couple perception with robotic control, offering a promising path toward general-purpose embodied intelligence. However, current SOTA VLAs are primarily pretrained on multimodal tasks with limited relevance to embodied scenarios, and then finetuned to map explicit instructions to actions. Consequently, due to the lack of reasoning-intensive pretraining and reasoning-guided manipulation, these models are unable to perform implicit human intention reasoning required for complex, real-world interactions. To overcome these limitations, we propose \textbf{IntentionVLA}, a VLA framework with a curriculum training paradigm and an efficient inference mechanism. Our proposed method first leverages carefully designed reasoning data that combine intention inference, spatial grounding, and compact embodied reasoning, endowing the model with both reasoning and perception capabilities. In the following finetuning stage, IntentionVLA employs the compact reasoning outputs as contextual guidance for action generation, enabling fast inference under indirect instructions. Experimental results show that IntentionVLA substantially outperforms $π_0$, achieving 18\% higher success rates with direct instructions and 28\% higher than ECoT under intention instructions. On out-of-distribution intention tasks, IntentionVLA achieves over twice the success rate of all baselines, and further enables zero-shot human-robot interaction with 40\% success rate. These results highlight IntentionVLA as a promising paradigm for next-generation human-robot interaction (HRI) systems.

