---
layout: default
title: FastPose-ViT: A Vision Transformer for Real-Time Spacecraft Pose Estimation
---

# FastPose-ViT: A Vision Transformer for Real-Time Spacecraft Pose Estimation

**arXiv**: [2512.09792v1](https://arxiv.org/abs/2512.09792) | [PDF](https://arxiv.org/pdf/2512.09792.pdf)

**作者**: Pierre Ancey, Andrew Price, Saqib Javed, Mathieu Salzmann

**分类**: cs.CV

**发布日期**: 2025-12-10

**备注**: Accepted to WACV 2026. Preprint version

---

## 💡 一句话要点

**提出FastPose-ViT，用于资源受限平台上的航天器实时姿态估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `航天器姿态估计` `Vision Transformer` `实时性` `边缘计算` `6DoF姿态估计`

## 📋 核心要点

1. 现有航天器姿态估计方法依赖迭代PnP算法，计算量大，难以在资源受限设备上实时部署。
2. FastPose-ViT基于ViT直接回归6DoF姿态，并提出新的数学形式，将局部预测映射到全局。
3. 实验表明，FastPose-ViT性能优于非PnP方法，与PnP方法相当，并在边缘设备上实现实时性能。

## 📝 摘要（中文）

本文提出了一种基于Vision Transformer (ViT)的FastPose-ViT架构，用于直接回归航天器的6自由度(6DoF)姿态，旨在解决现有基于迭代Perspective-n-Point (PnP)算法计算密集、不适用于资源受限边缘设备实时部署的问题。该方法处理来自目标边界框的裁剪图像，并引入了一种新的数学形式，将这些局部预测映射回完整图像尺度。该形式源于射影几何原理和“视在旋转”的概念，模型预测一个视在旋转矩阵，然后对其进行校正以找到真实的姿态。实验表明，该方法优于其他非PnP策略，并在SPEED数据集上实现了与最先进的PnP方法相媲美的性能。此外，通过量化模型并将其部署在功耗受限的边缘硬件上，验证了其在实际空间任务中的适用性。在NVIDIA Jetson Orin Nano上，端到端流水线在顺序执行下实现了约75毫秒/帧的延迟，在并发调度阶段实现了高达33 FPS的非阻塞吞吐量。

## 🔬 方法详解

**问题定义**：论文旨在解决航天器6DoF姿态估计问题，尤其是在资源受限的边缘设备上进行实时姿态估计。现有方法，特别是基于迭代PnP算法的方法，计算复杂度高，难以满足实时性要求，限制了其在实际空间任务中的应用。

**核心思路**：论文的核心思路是利用Vision Transformer (ViT)直接回归6DoF姿态，避免迭代计算。通过学习图像特征与姿态之间的直接映射关系，降低计算复杂度，提高推理速度。此外，论文还引入了一种新的数学形式，将裁剪图像的局部姿态预测映射回完整图像的全局姿态。

**技术框架**：FastPose-ViT的整体框架包括以下几个主要阶段：1) 输入裁剪后的航天器图像；2) 使用ViT提取图像特征；3) 通过回归头预测视在旋转矩阵；4) 利用提出的数学形式，将视在旋转矩阵校正为真实的旋转矩阵，并预测平移向量。整个流程是端到端可训练的。

**关键创新**：论文的关键创新在于提出了一种新的数学形式，用于将裁剪图像的局部姿态预测映射回完整图像的全局姿态。这种方法基于射影几何和“视在旋转”的概念，通过预测一个视在旋转矩阵，然后对其进行校正，从而得到真实的旋转矩阵。这种方法避免了直接回归全局姿态的困难，提高了模型的精度和鲁棒性。

**关键设计**：FastPose-ViT使用标准的ViT架构作为特征提取器。损失函数包括旋转损失和平移损失。旋转损失可以使用四元数损失或旋转矩阵损失。平移损失可以使用L1或L2损失。关键参数包括ViT的层数、头数、嵌入维度等。此外，视在旋转矩阵的校正过程也需要仔细设计，以保证校正的准确性。

## 📊 实验亮点

FastPose-ViT在SPEED数据集上取得了与最先进的PnP方法相媲美的性能，同时显著降低了计算复杂度。在NVIDIA Jetson Orin Nano上，该方法实现了约75毫秒/帧的延迟，以及高达33 FPS的非阻塞吞吐量，验证了其在资源受限边缘设备上的实时性能。实验结果表明，FastPose-ViT是一种高效、准确的航天器姿态估计方法。

## 🎯 应用场景

该研究成果可应用于在轨服务、空间碎片移除、自主导航等航天任务中。通过在资源受限的边缘设备上实现实时姿态估计，可以提高航天器的自主性和智能化水平，降低对地面站的依赖，从而降低任务成本，提高任务效率。该方法还可推广到其他需要实时姿态估计的场景，如机器人导航、增强现实等。

## 📄 摘要（原文）

> Estimating the 6-degrees-of-freedom (6DoF) pose of a spacecraft from a single image is critical for autonomous operations like in-orbit servicing and space debris removal. Existing state-of-the-art methods often rely on iterative Perspective-n-Point (PnP)-based algorithms, which are computationally intensive and ill-suited for real-time deployment on resource-constrained edge devices. To overcome these limitations, we propose FastPose-ViT, a Vision Transformer (ViT)-based architecture that directly regresses the 6DoF pose. Our approach processes cropped images from object bounding boxes and introduces a novel mathematical formalism to map these localized predictions back to the full-image scale. This formalism is derived from the principles of projective geometry and the concept of "apparent rotation", where the model predicts an apparent rotation matrix that is then corrected to find the true orientation. We demonstrate that our method outperforms other non-PnP strategies and achieves performance competitive with state-of-the-art PnP-based techniques on the SPEED dataset. Furthermore, we validate our model's suitability for real-world space missions by quantizing it and deploying it on power-constrained edge hardware. On the NVIDIA Jetson Orin Nano, our end-to-end pipeline achieves a latency of ~75 ms per frame under sequential execution, and a non-blocking throughput of up to 33 FPS when stages are scheduled concurrently.

