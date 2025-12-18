---
layout: default
title: Towards Transferable Defense Against Malicious Image Edits
---

# Towards Transferable Defense Against Malicious Image Edits

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14341" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14341v1</a>
  <a href="https://arxiv.org/pdf/2512.14341.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14341v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14341v1', 'Towards Transferable Defense Against Malicious Image Edits')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 14 pages, 5 figures

---

## 💡 一句话要点

**提出TDAE框架，增强图像对恶意编辑的防御迁移能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `对抗防御` `恶意编辑` `图像编辑` `扩散模型` `可迁移性` `梯度正则化` `文本嵌入` `双模态学习`

## 📋 核心要点

1. 现有防御方法在跨不同扩散模型时，防御恶意图像编辑的迁移能力不足，鲁棒性较差。
2. TDAE框架通过图像和文本的协同优化，增强图像对恶意编辑的免疫力，提高防御的迁移性。
3. 实验结果表明，TDAE在模型内和跨模型评估中，均能有效减轻恶意编辑，达到最佳性能。

## 📝 摘要（中文）

现有方法在对抗基于扩散模型的图像编辑系统中恶意操作时，通过在输入图像中加入不易察觉的扰动，展现出了一定的潜力。然而，这些方法在跨模型评估中迁移性有限。为了解决这个问题，我们提出了可迁移的恶意图像编辑防御（TDAE），这是一个新颖的双模态框架，通过协调图像-文本优化来增强图像对恶意编辑的免疫力。具体来说，在视觉防御层面，我们引入了FlatGrad防御机制（FDM），它将梯度正则化纳入对抗目标中。通过显式地引导扰动朝向平坦最小值，FDM增强了对未见编辑模型的免疫鲁棒性。对于文本增强保护，我们提出了一种名为动态提示防御（DPD）的对抗优化范式，它周期性地细化文本嵌入，以使免疫图像的编辑结果与原始图像的编辑结果对齐，然后使用优化的嵌入更新图像。通过对各种嵌入进行迭代对抗更新，DPD强制生成免疫图像，从而寻求更广泛的免疫增强特征，从而实现跨模型可迁移性。大量的实验结果表明，我们的TDAE在减轻模型内和跨模型评估中的恶意编辑方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决现有方法在防御基于扩散模型的恶意图像编辑时，跨模型迁移能力不足的问题。现有方法生成的对抗扰动往往依赖于特定的模型结构和参数，导致在面对未知的编辑模型时，防御效果显著下降。

**核心思路**：论文的核心思路是通过双模态（图像和文本）的协同优化，增强图像对恶意编辑的免疫力，并提高防御的迁移性。具体来说，通过在图像层面引入梯度正则化，使对抗扰动位于损失函数的平坦最小值区域，从而提高鲁棒性；同时，在文本层面通过动态提示防御，使免疫图像的编辑结果与原始图像保持一致。

**技术框架**：TDAE框架包含两个主要模块：FlatGrad防御机制（FDM）和动态提示防御（DPD）。FDM主要负责在视觉层面生成对抗扰动，通过梯度正则化增强图像的鲁棒性。DPD则在文本层面进行对抗优化，周期性地细化文本嵌入，使免疫图像的编辑结果与原始图像对齐。两个模块协同工作，共同增强图像对恶意编辑的防御能力。

**关键创新**：论文的关键创新在于提出了一个双模态的防御框架，将图像和文本信息结合起来，共同对抗恶意编辑。此外，FDM通过梯度正则化，显式地引导扰动朝向平坦最小值，提高了防御的鲁棒性。DPD通过动态调整文本嵌入，增强了防御的迁移性。

**关键设计**：FDM的关键设计在于梯度正则化项的引入，通过最小化扰动附近的梯度范数，使扰动位于损失函数的平坦最小值区域。DPD的关键设计在于周期性地更新文本嵌入，并使用更新后的嵌入来生成对抗样本。具体的损失函数和参数设置在论文中有详细描述，例如对抗损失函数，梯度正则化系数等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14341v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14341v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14341v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TDAE在减轻恶意编辑方面取得了显著的性能提升。在跨模型评估中，TDAE的防御效果优于现有的防御方法，实现了最先进的性能。具体的性能数据和对比基线在论文中有详细的展示，证明了TDAE的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于保护数字图像的完整性和安全性，例如防止恶意用户篡改图像内容，用于社交媒体平台、在线图像编辑工具、以及需要图像认证的场景。通过提高图像对恶意编辑的免疫力，可以有效防止虚假信息的传播和恶意攻击。

## 📄 摘要（原文）

> Recent approaches employing imperceptible perturbations in input images have demonstrated promising potential to counter malicious manipulations in diffusion-based image editing systems. However, existing methods suffer from limited transferability in cross-model evaluations. To address this, we propose Transferable Defense Against Malicious Image Edits (TDAE), a novel bimodal framework that enhances image immunity against malicious edits through coordinated image-text optimization. Specifically, at the visual defense level, we introduce FlatGrad Defense Mechanism (FDM), which incorporates gradient regularization into the adversarial objective. By explicitly steering the perturbations toward flat minima, FDM amplifies immune robustness against unseen editing models. For textual enhancement protection, we propose an adversarial optimization paradigm named Dynamic Prompt Defense (DPD), which periodically refines text embeddings to align the editing outcomes of immunized images with those of the original images, then updates the images under optimized embeddings. Through iterative adversarial updates to diverse embeddings, DPD enforces the generation of immunized images that seek a broader set of immunity-enhancing features, thereby achieving cross-model transferability. Extensive experimental results demonstrate that our TDAE achieves state-of-the-art performance in mitigating malicious edits under both intra- and cross-model evaluations.

