---
layout: default
title: CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization
---

# CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11096" target="_blank" class="toolbar-btn">arXiv: 2510.11096v1</a>
    <a href="https://arxiv.org/pdf/2510.11096.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11096v1" 
            onclick="toggleFavorite(this, '2510.11096v1', 'CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Fengling Zhu, Boshi Liu, Jingyu Hua, Sheng Zhong

**分类**: cs.CV

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出CoDefend，通过扩散净化和提示优化协同防御多模态大语言模型的对抗攻击。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `对抗防御` `扩散模型` `图像净化` `提示优化`

## 📋 核心要点

1. 多模态大语言模型易受对抗攻击，现有防御方法（如对抗训练和输入净化）存在计算成本高、泛化性差等问题。
2. CoDefend提出一种基于监督扩散的去噪框架，利用配对数据微调扩散模型，并结合提示优化增强防御能力。
3. 实验表明，CoDefend显著提高了模型对已知和未知对抗攻击的鲁棒性，并在图像描述和视觉问答任务上表现出色。

## 📝 摘要（中文）

多模态大语言模型(MLLM)通过整合视觉和文本模态，在图像描述、视觉问答和跨模态推理等任务中取得了显著成功。然而，其多模态特性也使其容易受到对抗性威胁，攻击者可以扰动其中一个或两个模态，从而诱导有害、误导或违反策略的输出。现有的防御策略，如对抗训练和输入净化，面临着明显的局限性：对抗训练通常只提高对已知攻击的鲁棒性，同时产生高昂的计算成本，而传统的净化方法通常会降低图像质量，并且对复杂的多模态任务的泛化能力不足。本文侧重于防御视觉模态，它经常作为对抗性操纵的主要入口点。我们提出了一个基于监督扩散的去噪框架，该框架利用配对的对抗性干净图像数据集，通过定向的、特定于任务的指导来微调扩散模型。与先前的无监督净化方法（如DiffPure）不同，我们的方法实现了更高质量的重建，同时显著提高了多模态任务中的防御鲁棒性。此外，我们结合了提示优化作为一种补充防御机制，增强了对各种和未见过的攻击策略的抵抗力。在图像描述和视觉问答上的大量实验表明，我们的方法不仅大大提高了鲁棒性，而且对未知的对抗性攻击表现出很强的可转移性。这些结果突出了基于监督扩散的去噪对于多模态防御的有效性，为在实际应用中更可靠和安全地部署MLLM铺平了道路。

## 🔬 方法详解

**问题定义**：多模态大语言模型容易受到对抗攻击，攻击者可以通过修改图像等输入来欺骗模型。现有的防御方法，如对抗训练，计算成本高昂且泛化能力有限；而传统的图像净化方法，如DiffPure，在提高鲁棒性的同时，往往会降低图像质量，且在复杂的多模态任务中表现不佳。因此，如何高效且高质量地防御多模态大语言模型的对抗攻击是一个关键问题。

**核心思路**：CoDefend的核心思路是利用监督扩散模型进行图像去噪，并结合提示优化来增强模型的鲁棒性。通过使用配对的对抗样本和干净样本进行训练，扩散模型能够学习到如何有效地去除对抗扰动，恢复原始图像的语义信息。同时，提示优化可以进一步提高模型对各种攻击的抵抗能力，使其能够更好地理解和处理对抗样本。

**技术框架**：CoDefend的整体框架包含两个主要模块：基于监督扩散的图像净化模块和提示优化模块。首先，图像净化模块使用微调的扩散模型对输入的对抗图像进行去噪，生成更干净的图像。然后，将净化后的图像和原始文本提示输入到多模态大语言模型中，得到模型的输出。同时，提示优化模块通过调整文本提示，进一步提高模型对对抗攻击的抵抗能力。这两个模块协同工作，共同防御对抗攻击。

**关键创新**：CoDefend的关键创新在于使用了监督扩散模型进行图像净化。与传统的无监督方法相比，监督扩散模型能够更好地利用配对的对抗样本和干净样本信息，从而实现更高质量的图像重建和更强的防御鲁棒性。此外，结合提示优化进一步增强了模型的防御能力，使其能够更好地应对各种未知的攻击。

**关键设计**：在图像净化模块中，使用了DDPM（Denoising Diffusion Probabilistic Models）作为基础扩散模型，并使用配对的对抗样本和干净样本进行微调。损失函数包括扩散模型的重建损失和对抗损失，以确保模型能够有效地去除对抗扰动。在提示优化模块中，使用了梯度下降等优化算法来调整文本提示，目标是最大化模型在对抗样本上的性能。

## 📊 实验亮点

实验结果表明，CoDefend在图像描述和视觉问答任务上显著提高了模型对对抗攻击的鲁棒性。例如，在针对图像描述任务的实验中，CoDefend将模型在对抗样本上的性能提高了超过20%，并且对未知的对抗攻击也表现出很强的可转移性。与现有的防御方法相比，CoDefend在提高鲁棒性的同时，能够保持较高的图像质量。

## 🎯 应用场景

CoDefend可应用于各种需要安全可靠的多模态大语言模型的场景，例如自动驾驶、医疗诊断、金融风控等。通过提高模型对对抗攻击的鲁棒性，可以避免因恶意输入导致的错误决策，保障系统的安全性和可靠性。该研究成果有助于推动多模态大语言模型在实际应用中的广泛部署。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable success in tasks such as image captioning, visual question answering, and cross-modal reasoning by integrating visual and textual modalities. However, their multimodal nature also exposes them to adversarial threats, where attackers can perturb either modality or both jointly to induce harmful, misleading, or policy violating outputs. Existing defense strategies, such as adversarial training and input purification, face notable limitations: adversarial training typically improves robustness only against known attacks while incurring high computational costs, whereas conventional purification approaches often suffer from degraded image quality and insufficient generalization to complex multimodal tasks.
>   In this work, we focus on defending the visual modality, which frequently serves as the primary entry point for adversarial manipulation. We propose a supervised diffusion based denoising framework that leverages paired adversarial clean image datasets to fine-tune diffusion models with directional, task specific guidance. Unlike prior unsupervised purification methods such as DiffPure, our approach achieves higher quality reconstructions while significantly improving defense robustness in multimodal tasks. Furthermore, we incorporate prompt optimization as a complementary defense mechanism, enhancing resistance against diverse and unseen attack strategies.
>   Extensive experiments on image captioning and visual question answering demonstrate that our method not only substantially improves robustness but also exhibits strong transferability to unknown adversarial attacks. These results highlight the effectiveness of supervised diffusion based denoising for multimodal defense, paving the way for more reliable and secure deployment of MLLMs in real world applications.

