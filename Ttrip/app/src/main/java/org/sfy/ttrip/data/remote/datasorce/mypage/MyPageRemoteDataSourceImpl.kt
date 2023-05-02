package org.sfy.ttrip.data.remote.datasorce.mypage

import org.sfy.ttrip.data.remote.service.MyPageApiService
import javax.inject.Inject

class MyPageRemoteDataSourceImpl @Inject constructor(
    private val myPageApiService: MyPageApiService
) : MyPageRemoteDataSource {

    override suspend fun updateUserInfo(body: UpdateUserInfoRequest) {
        myPageApiService.updateUserInfo(body)
    }
}